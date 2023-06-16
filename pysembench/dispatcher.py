from pysembench.handler import PysubytHandler, PyshaclHandler


class TaskDispatcher:
    type_to_handler = {
        "pysubyt": PysubytHandler,
        "pyshacl": PyshaclHandler,
    }

    def dispatch(self, task):
        handler = self.type_to_handler[task.config["type"].lower()]
        handler().handle(task)
