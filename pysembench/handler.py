import logging
import os

from pyshacl import validate
from pysubyt import Subyt
from syncfstriples import SyncFsTriples
from travharv import TravHarv

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
        Subyt(**task.args).process()


class PySyncFsTriplesHandler(TaskHandler):
    def handle(self, task):
        SyncFsTriples(**task.args).process()


class PyTravHarvHandler(TaskHandler):
    def handle(self, task):
        TravHarv(**task.args).process()


class RMLHandler(TaskHandler):
    ...
