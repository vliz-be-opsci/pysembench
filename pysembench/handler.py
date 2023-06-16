import logging
import os
import subprocess
from pyshacl import validate

logger = logging.getLogger(__name__)


class TaskHandler:
    def handle(self):
        raise NotImplementedError


class CSVWHandler(TaskHandler):
    ...


class EyereasonerHandler(TaskHandler):
    ...


class Pykg2tblHandler(TaskHandler):
    ...


class PyshaclHandler(TaskHandler):
    def handle(self, task):
        conforms, _, _ = validate(
            data_graph=os.path.join(
                task.input_data_location,
                task.config["data_graph"]
            ),
            shacl_graph=os.path.join(
                task.sembench_data_location,
                task.config["shacl_graph"]
            ),
            data_graph_format="ttl",
            shacl_graph_format="ttl",
            inference="rdfs",
            debug=True,
        )
        assert conforms, (
            "pyshacl validation failed for "
            f"data graph \"{task.config['data_graph']}\" "
            "with "
            f"shape graph \"{task.config['shacl_graph']}\""
        )
        return conforms


class PysubytHandler(TaskHandler):
    def handle(self, task):
        """Construct a shell command based on the Task attributes and run it
        via a subprocess call.
        """
        input = task.config.get("input") or ""
        if input:
            input = f'--input "{os.path.join(task.input_data_location, input)}"'

        output = os.path.join(
            task.output_data_location, task.config["output"]
        )

        templates = os.path.join(
            task.sembench_data_location, task.config["template"]["jinja_root"]
        )

        name = task.config["template"]["file_name"]

        sets = task.config.get("sets") or ""
        if sets:
            sets_buffer = ""
            for set_key, set_value in sets.items():
                set_name = set_key
                file_name = os.path.join(task.input_data_location, set_value)
                sets_buffer += f'--set "{set_name}" "{file_name}" '
            sets = sets_buffer

        variables = task.config.get("variables") or ""
        if variables:
            variables_buffer = ""
            for variable_key, variable_value in variables.items():
                variables_buffer += f'--var "{variable_key}" "{variable_value}" '
            variables = variables_buffer

        mode = task.config.get("mode") or "iteration"

        force = "--force" if task.force else ""

        cmd = (
            f'pysubyt {force} '
            f'{input} --output "{output}" '
            f'--templates "{templates}" --name "{name}" '
            f'{sets}'
            f'{variables}'
            f'--mode "{mode}"'
        )
        logger.info(f"subprocess call; {cmd}")
        subprocess.check_call(cmd, shell=True)
        return cmd


class RMLHandler(TaskHandler):
    ...
