# Example usage

The following `sembench.yaml` config file defines two tasks: one to run with pysubyt and another one to run with pyshacl.

```yaml
rdf_production_task:
  func: pysubyt
  args:
    template_folder: !resolve "{home}/templates"
    template_name: data.ttl.j2
    source: !resolve "{input}/data.csv"
    extra_sources:
      countries: !resolve "{input}/country_codes.csv"
    sink: !resolve "{output}/data.ttl"
    mode: no-iteration

rdf_validation_task:
  func: pyshacl
  args:
    data_graph: example_data_conform.ttl
    shacl_graph: example_shape.ttl
```

All tasks in the `sembench.yaml` config file can be processed as follows.

```python
from pysembench import Sembench

sb = Sembench(
    locations={
        "home": "./examples/resources/sembench_data",
        "input": "./examples/resources/input_data",
    }
)

sb.process()
```

<p align="center">
<a href="https://github.com/JotaFan/pycoverage"><img src="https://github.com/vliz-be-opsci/pysembench/tree/gh-pages/coverage.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>
