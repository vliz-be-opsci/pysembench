"""
This script generates examples/resources/input_data/data.ttl via pysubyt and
validates examples/resources/input_data/example_data_conform.ttl via pyshacl.
Modify examples/resources/sembench_data/sembench.json to run pyshacl on
examples/resources/input_data/example_data_nonconform.ttl and see how the
process fails.
"""
from pysembench import Sembench

sb = Sembench(
    locations={
        "home": "./examples/resources/sembench_data",
        "input": "./examples/resources/input_data",
    }
)

sb.process()
