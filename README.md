# Example usage

The following `sembench.json` config file defines a single task to be run with pysubyt:

```json
[
    {
        "type": "pysubyt",
        "input": "data.csv",
        "output": "data.ttl",
        "template": {"jinja_root": "templates", "file_name": "data.ttl.j2"},
        "sets": {
            "countries": "countries.csv",
        },
        "mode": "no-iteration"
    }
]
```

All tasks in the `sembench.json` config file can be processed as follows. Keep in mind to place the `process` method in a `__main__` block, as the tasks are run in parallel.

```python
from pysembench.core import Sembench

sb = Sembench(
    input_data_location="./tests/resources/input_data",
    sembench_data_location="./tests/resources/sembench_data",
)

if __name__ == "__main__":
    sb.process(force=True)
```

<p align="center">
<a href="https://github.com/JotaFan/pycoverage"><img src="https://github.com/vliz-be-opsci/pysembench/tree/gh-pages/docs/build/html/coverage.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>