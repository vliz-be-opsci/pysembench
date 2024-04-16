import logging
import os
import time

import yaml
from apscheduler.schedulers.blocking import BlockingScheduler
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from pysembench.dispatcher import TaskDispatcher
from pysembench.task import Task

logger = logging.getLogger(__name__)


class ConfigFileEventHandler(FileSystemEventHandler):
    def __init__(self, sembench_config_path, func):
        super().__init__()
        self.sembench_config_path = sembench_config_path
        self.func = func
        os.environ["PYSEMBENCH_WATCHDOG_TIME"] = "0"

    def on_modified(self, event):
        if event.src_path == self.sembench_config_path:
            time_elapsed = time.time() - float(
                os.environ["PYSEMBENCH_WATCHDOG_TIME"]
            )
            if time_elapsed < 2:
                pass
            else:
                try:
                    self.func()
                except Exception as e:
                    raise e
                finally:
                    os.environ["PYSEMBENCH_WATCHDOG_TIME"] = str(time.time())


class Sembench:
    def __init__(
        self,
        input_data_location,
        output_data_location=None,
        sembench_data_location=None,
        sembench_config_path=None,
        sembench_config_file_name=None,
        scheduler_interval_seconds=None,
        watch_config_file=False,
        fail_fast=False,
    ):
        """Create a Sembench object.

        :param input_data_location: Path to the input data folder.

        :param output_data_location: Path to the output data folder. Optional;
        defaults to the input_data_location.

        :param sembench_data_location: Path to the sembench data folder.
        Optional; defaults to the input_data_location.

        :param sembench_config_path: Path to the sembench config file.
        Optional; defaults to sembench_data_location/sembench.json.

        :param sembench_config_file_name: Name of the sembench config file.
        Optional; defaults to sembench.json.

        :returns: None
        """
        assert input_data_location, "input_data_location must be specified"
        self.input_data_location = input_data_location
        self.output_data_location = output_data_location or input_data_location
        self.sembench_data_location = (
            sembench_data_location or input_data_location
        )
        self.sembench_config_path = sembench_config_path
        self.sembench_config_file_name = sembench_config_file_name
        self.scheduler_interval_seconds = scheduler_interval_seconds
        self.watch_config_file = watch_config_file
        self.fail_fast = fail_fast

        assert not (self.sembench_config_path and sembench_config_file_name), (
            "sembench_config_file_name can't be specified when "
            "sembench_config_path is specified"
        )

        self.sembench_config_path = (
            self.sembench_config_path or self.sembench_data_location
        )
        self.sembench_config_file_name = (
            self.sembench_config_file_name or "sembench.yaml"
        )

        if not self.sembench_config_path.endswith(
            self.sembench_config_file_name
        ):
            self.sembench_config_path = os.path.join(
                self.sembench_config_path, self.sembench_config_file_name
            )

        self.task_configs = yaml.safe_load(open(self.sembench_config_path))
        assert isinstance(self.task_configs, dict)

    @staticmethod
    def dispatch_task(task):
        TaskDispatcher().dispatch(task)

    def _process(self):
        tasks = [
            Task(
                input_data_location=self.input_data_location,
                output_data_location=self.output_data_location,
                sembench_data_location=self.sembench_data_location,
                task_id=task_id,
                func=task_config["func"],
                args=task_config["args"],
            )
            for task_id, task_config in self.task_configs.items()
        ]
        for task in tasks:
            try:
                self.dispatch_task(task)
            except Exception as e:
                logger.error(f"{task.task_id} failed with exception: {e}")
                if self.fail_fast:
                    raise e

    def process(self):
        if self.watch_config_file:
            config_file_event_handler = ConfigFileEventHandler(
                self.sembench_config_path,
                self._process,
            )
            observer = Observer()
            observer.schedule(
                event_handler=config_file_event_handler,
                path=self.sembench_data_location,
            )
            observer.start()

            try:
                self._process()
                if self.scheduler_interval_seconds:
                    scheduler = BlockingScheduler()
                    scheduler.add_job(
                        self._process,
                        "interval",
                        seconds=int(self.scheduler_interval_seconds),
                    )
                    scheduler.start()
                else:
                    while True:
                        pass
            except KeyboardInterrupt:
                observer.stop()
            observer.join()

        else:
            self._process()
            if self.scheduler_interval_seconds:
                scheduler = BlockingScheduler()
                scheduler.add_job(
                    self._process,
                    "interval",
                    seconds=int(self.scheduler_interval_seconds),
                )
                scheduler.start()
