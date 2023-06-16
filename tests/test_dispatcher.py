import os

from pysembench.dispatcher import TaskDispatcher
from tests.util4tests import tasks


def test_dispacher_dispatch():
    # TODO: build tests for function inside TaskDispacher
    task_dispacher = TaskDispatcher()
    task_dispacher.dispatch(tasks[0])
    os.remove("./OUTPUT")
    assert type(task_dispacher) == TaskDispatcher
