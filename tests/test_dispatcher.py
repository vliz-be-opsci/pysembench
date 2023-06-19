from unittest import TestCase
from unittest.mock import Mock, patch

from pysembench.dispatcher import TaskDispatcher
from pysembench.handler import PyshaclHandler, PysubytHandler
from pysembench.task import Task


class TestTaskDispatcher(TestCase):
    @patch("pysembench.handler.PysubytHandler.handle")
    @patch("pysembench.handler.PyshaclHandler.handle")
    def test_dispatch(self, patch1, patch2):
        patch1 = Mock()  # noqa F841
        patch2 = Mock()  # noqa F841
        task1 = Task(".", ".", ".", {"type": "pysubyt"}, True)
        task2 = Task(".", ".", ".", {"type": "pyshacl"}, True)
        self.assertEqual(TaskDispatcher().dispatch(task1), PysubytHandler)
        self.assertEqual(TaskDispatcher().dispatch(task2), PyshaclHandler)
