# Example usage

The following `sembench.yaml` config file defines two tasks: one to run with pysubyt and another one to run with pyshacl.

```yaml
rdf_production_task:
  type: pysubyt
  input: data.csv
  output: data.ttl
  template:
    jinja_root: templates
    file_name: data.ttl.j2
  sets:
    countries: country_codes.csv
  mode: no-iteration
  force: true

rdf_validation_task:
  type: pyshacl
  data_graph: example_data_conform.ttl
  shacl_graph: example_shape.ttl

```

All tasks in the `sembench.yaml` config file can be processed as follows.

```python
from pysembench import Sembench

sb = Sembench(
    input_data_location="./examples/resources/input_data",
    sembench_data_location="./examples/resources/sembench_data",
)

sb.process()
```

<p align="center">
<a href="https://github.com/JotaFan/pycoverage"><img src="https://github.com/vliz-be-opsci/pysembench/tree/gh-pages/coverage.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>
