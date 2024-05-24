"""
This script runs pysembench with scheduling at a 10 second interval.
"""
from pysembench import Sembench

sb = Sembench(
    locations={
        "home": "./examples/resources/sembench_data",
        "input": "./examples/resources/input_data",
    },
    scheduler_interval_seconds=10,
)

sb.process()
