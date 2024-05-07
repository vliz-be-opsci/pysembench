#! /usr/bin/env python
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
        task1 = Task(".", ".", ".", "my_pysubyt_task", "pysubyt", {})
        task2 = Task(".", ".", ".", "my_pyshacl_task", "pyshacl", {})
        self.assertEqual(TaskDispatcher().dispatch(task1), PysubytHandler)
        self.assertEqual(TaskDispatcher().dispatch(task2), PyshaclHandler)


if __name__ == "__main__":
    from util4tests import run_single_test

    run_single_test(__file__)
