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
        "variables": {
            "base_uri": "https://vliz-be-opsci.github.io/"
        },
        "mode": "no-iteration"
    }
]
```

All tasks in the `sembench.json` config file can be processed as follows.

```python
from pysembench import Sembench

sb = Sembench(
    input_data_location="./examples/resources/input_data",
    sembench_data_location="./examples/resources/sembench_data",
    force=True
)

sb.process()
```

<p align="center">
<a href="https://github.com/JotaFan/pycoverage"><img src="https://github.com/vliz-be-opsci/pysembench/tree/gh-pages/coverage.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>
