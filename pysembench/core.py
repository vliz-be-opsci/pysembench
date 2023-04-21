import json
import os

from .dispatcher import TaskDispatcher
from .task import Task


class Sembench:
    def __init__(
        self,
        input_data_location,
        output_data_location=None,
        sembench_data_location=None,
        sembench_config_path=None,
        sembench_config_file_name=None,
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
        self.input_data_location = input_data_location
        self.output_data_location = output_data_location or input_data_location
        self.sembench_data_location = (
            sembench_data_location or input_data_location
        )
        self.sembench_config_path = sembench_config_path
        self.sembench_config_file_name = sembench_config_file_name

        assert not (self.sembench_config_path and sembench_config_file_name), (
            "sembench_config_file_name can't be specified when "
            "sembench_config_path is specified"
        )

        self.sembench_config_path = (
            self.sembench_config_path or self.sembench_data_location
        )
        self.sembench_config_file_name = (
            self.sembench_config_file_name or "sembench.json"
        )

        if not self.sembench_config_path.endswith(
            self.sembench_config_file_name
        ):
            self.sembench_config_path = os.path.join(
                self.sembench_config_path, self.sembench_config_file_name
            )

        self.configs = []

        with open(self.sembench_config_path) as f:
            self.configs = json.loads(f.read())

        assert type(self.configs) == list

    @staticmethod
    def dispatch_task(task):
        TaskDispatcher().dispatch(task)

    def process(self, force=False):
        tasks = [
            Task(
                input_data_location=self.input_data_location,
                output_data_location=self.output_data_location,
                sembench_data_location=self.sembench_data_location,
                config=config,
                force=force,
            )
            for config in self.configs
        ]
        for task in tasks:
            self.dispatch_task(task)
