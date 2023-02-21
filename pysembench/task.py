class Task:
    def __init__(
        self,
        input_data_location,
        output_data_location,
        sembench_data_location,
        config,
        force,
    ):
        self.input_data_location = input_data_location
        self.output_data_location = output_data_location
        self.sembench_data_location = sembench_data_location
        self.config = config
        self.force = force
