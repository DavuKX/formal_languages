class Invoker:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def execute_command(self, obj1, obj2):
        if self.command:
            return self.command.execute(obj1, obj2)