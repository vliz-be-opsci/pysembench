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
