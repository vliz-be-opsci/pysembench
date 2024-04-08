import logging
import os
import subprocess

from pyshacl import validate
from travharv import TravHarv
from syncfstriples import SyncFsTriples

logger = logging.getLogger(__name__)


class TaskHandler:
    def handle(self):
        raise NotImplementedError


class CSVWHandler(TaskHandler): ...


class EyereasonerHandler(TaskHandler): ...


class Pykg2tblHandler(TaskHandler): ...


class PyshaclHandler(TaskHandler):
    def handle(self, task):
        conforms, _, _ = validate(
            data_graph=os.path.join(
                task.input_data_location, task.args["data_graph"]
            ),
            shacl_graph=os.path.join(
                task.sembench_data_location, task.args["shacl_graph"]
            ),
            data_graph_format="ttl",
            shacl_graph_format="ttl",
            inference="rdfs",
            debug=True,
        )
        assert conforms, (
            "pyshacl validation failed for "
            f"data graph \"{task.args['data_graph']}\" "
            "with "
            f"shape graph \"{task.args['shacl_graph']}\""
        )
        return conforms


class PysubytHandler(TaskHandler):
    def handle(self, task):
        """Construct a shell command based on the Task attributes and run it
        via a subprocess call.
        """
        input = task.args.get("input") or ""
        if input:
            input = (
                f'--input "{os.path.join(task.input_data_location, input)}"'
            )

        output = os.path.join(task.output_data_location, task.args["output"])

        templates = os.path.join(
            task.sembench_data_location, task.args["template"]["jinja_root"]
        )

        name = task.args["template"]["file_name"]

        sets = task.args.get("sets") or ""
        if sets:
            sets_buffer = ""
            for set_key, set_value in sets.items():
                set_name = set_key
                file_name = os.path.join(task.input_data_location, set_value)
                sets_buffer += f'--set "{set_name}" "{file_name}" '
            sets = sets_buffer

        variables = task.args.get("variables") or ""
        if variables:
            variables_buffer = ""
            for variable_key, variable_value in variables.items():
                variables_buffer += (
                    f'--var "{variable_key}" "{variable_value}" '
                )
            variables = variables_buffer

        mode = task.args.get("mode") or "iteration"

        force = "--force" if (task.args.get("force") is True) else ""

        cmd = (
            f"pysubyt {force} "
            f'{input} --output "{output}" '
            f'--templates "{templates}" --name "{name}" '
            f"{sets}"
            f"{variables}"
            f'--mode "{mode}"'
        )
        logger.info(f"subprocess call; {cmd}")  # noqa E702
        subprocess.check_call(cmd, shell=True)
        return cmd


class PySyncFsTriplesHandler(TaskHandler):
    def handle(self, task):
        SyncFsTriples(**task.args).process()


class PyTravHarvHandler(TaskHandler):
    def handle(self, task):
        TravHarv(**task.args).process()


class RMLHandler(TaskHandler): ...
