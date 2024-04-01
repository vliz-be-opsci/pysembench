"""
This script runs pysembench with scheduling at a 10 second interval.
"""
from pysembench import Sembench

sb = Sembench(
    input_data_location="./examples/resources/input_data",
    sembench_data_location="./examples/resources/sembench_data",
    scheduler_interval_seconds=10,
)

sb.process()