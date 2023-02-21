from .handler import PysubytHandler


class TaskDispatcher:
    type_to_handler = {
        "pysubyt": PysubytHandler,
    }

    def dispatch(self, task):
        handler = self.type_to_handler[task.config["type"].lower()]
        handler().handle(task)
