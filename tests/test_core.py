import os
from unittest import TestCase

from pysembench.core import Sembench


class TestSembench(TestCase):
    """Assert whether a Sembench object is properly initialized, depending on
    which keyword arguments are provided.
    """

    def test_init_input_data(self):
        kwargs = {
            "input_data_location": "./tests/resources/input_data",
        }
        sb = Sembench(**kwargs)
        self.assertEqual(sb.output_data_location, sb.input_data_location)
        self.assertEqual(sb.sembench_data_location, sb.input_data_location)
        self.assertEqual(
            sb.sembench_config_path,
            os.path.join(
                sb.sembench_data_location, sb.sembench_config_file_name
            ),
        )
        self.assertEqual(sb.sembench_config_file_name, "sembench.json")
        self.assertEqual(sb.configs[0]["type"], "A")

    def test_init_input_data_output_data(self):
        kwargs = {
            "input_data_location": "./tests/resources/input_data",
            "output_data_location": "./tests/resources/output_data",
        }
        sb = Sembench(**kwargs)
        self.assertEqual(
            sb.output_data_location, "./tests/resources/output_data"
        )
        self.assertEqual(sb.sembench_data_location, sb.input_data_location)
        self.assertEqual(
            sb.sembench_config_path,
            os.path.join(
                sb.sembench_data_location, sb.sembench_config_file_name
            ),
        )
        self.assertEqual(sb.sembench_config_file_name, "sembench.json")
        self.assertEqual(sb.configs[0]["type"], "A")

    def test_init_input_data_sembench_data(self):
        kwargs = {
            "input_data_location": "./tests/resources/input_data",
            "sembench_data_location": "./tests/resources/sembench_data",
        }
        sb = Sembench(**kwargs)
        self.assertEqual(sb.output_data_location, sb.input_data_location)
        self.assertEqual(
            sb.sembench_data_location, "./tests/resources/sembench_data"
        )
        self.assertEqual(
            sb.sembench_config_path,
            os.path.join(
                sb.sembench_data_location, sb.sembench_config_file_name
            ),
        )
        self.assertEqual(sb.sembench_config_file_name, "sembench.json")
        self.assertEqual(sb.configs[0]["type"], "B")

    def test_init_input_data_sembench_config_path(self):
        kwargs = {
            "input_data_location": "./tests/resources/input_data",
            "sembench_config_path": "./tests/resources/weirdly_named_sembench.json",  # noqa
        }
        sb = Sembench(**kwargs)
        self.assertEqual(sb.output_data_location, sb.input_data_location)
        self.assertEqual(sb.sembench_data_location, sb.input_data_location)
        self.assertEqual(
            sb.sembench_config_path,
            "./tests/resources/weirdly_named_sembench.json",
        )
        self.assertEqual(sb.sembench_config_file_name, "sembench.json")
        self.assertEqual(sb.configs[0]["type"], "C")

    def test_init_input_data_sembench_config_file_name(self):
        kwargs = {
            "input_data_location": "./tests/resources/input_data",
            "sembench_config_file_name": "another_weirdly_named_sembench.json",
        }
        sb = Sembench(**kwargs)
        self.assertEqual(sb.output_data_location, sb.input_data_location)
        self.assertEqual(sb.sembench_data_location, sb.input_data_location)
        self.assertEqual(
            sb.sembench_config_path,
            os.path.join(
                sb.sembench_data_location, sb.sembench_config_file_name
            ),
        )
        self.assertEqual(
            sb.sembench_config_file_name, "another_weirdly_named_sembench.json"
        )
        self.assertEqual(sb.configs[0]["type"], "D")

    def test_init_sembench_config_path_sembench_config_file_name(self):
        kwargs = {
            "input_data_location": "./tests/resources/input_data",
            "sembench_config_path": "./tests/resources/weirdly_named_sembench.json",  # noqa
            "sembench_config_file_name": "another_weirdly_named_sembench.json",
        }
        self.assertRaises(AssertionError, lambda: Sembench(**kwargs))
