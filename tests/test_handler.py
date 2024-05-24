#! /usr/bin/env python
from pathlib import Path
from unittest import TestCase

from pysembench.handler import PyshaclHandler
from pysembench.task import Task


class TestPyshaclHandler(TestCase):
    def test_handle(self):
        task = Task(
            Path("./tests/resources/input_data"),
            Path("."),
            Path("./tests/resources/sembench_data"),
            "my_pyshacl_task1",
            "pyshacl",
            {
                "data_graph": "example_data_conform.ttl",
                "shacl_graph": "example_shape.ttl",
            },
        )
        self.assertTrue(PyshaclHandler().handle(task))

        task = Task(
            Path("./tests/resources/input_data"),
            Path("."),
            Path("./tests/resources/sembench_data"),
            "my_pyshacl_task2",
            "pyshacl",
            {
                "data_graph": "example_data_nonconform.ttl",
                "shacl_graph": "example_shape.ttl",
            },
        )
        with self.assertRaises(AssertionError):
            PyshaclHandler().handle(task)


if __name__ == "__main__":
    from util4tests import run_single_test

    run_single_test(__file__)
