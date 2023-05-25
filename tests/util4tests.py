from itertools import product

from pysembench.task import Task

force = [False, True]
input = [None, "INPUT"]
output = ["OUTPUT"]
template_jinja_root = ["TEMPLATE_JINJA_ROOT"]
template_file_name = ["TEMPLATE_FILE_NAME"]
sets = [None, {"SET_KEY_1": "SET_VALUE_1", "SET_KEY_2": "SET_VALUE_2"}]
mode = [None, "MODE"]

grid = list(
    product(
        force,
        input,
        output,
        template_jinja_root,
        template_file_name,
        sets,
        mode,
    )
)

tasks = [
    Task(
        ".",
        ".",
        ".",
        {
            "type": "pysubyt",
            "input": g[1],
            "output": g[2],
            "template": {"jinja_root": g[3], "file_name": g[4]},
            "sets": g[5],
            "mode": g[6],
        },
        g[0],
    )
    for g in grid
]
