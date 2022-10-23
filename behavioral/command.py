"""
- An object provides some commands which are executed by some other object (invoker)
- Used in commands invoking system
"""
from abc import ABCMeta, abstractmethod


# Receiver
class Switch(object):
    @staticmethod
    def switch_on(text):
        print(f'Switch On: {text}')

    @staticmethod
    def switch_off(text):
        print(f'Switch off: {text}')


# Command
class Command(metaclass=ABCMeta):
    def __init__(self, receiver, text):
        self.receiver = receiver
        self.text = text

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class SwitchOnCommand(Command):
    def __init__(self, receiver, text):
        super().__init__(receiver, text)

    def execute(self):
        self.receiver.switch_on(self.text)

    def undo(self):
        self.receiver.switch_off(f'Undoing: {self.text}')


class SwitchOffCommand(Command):
    def __init__(self, receiver, text):
        super().__init__(receiver, text)

    def execute(self):
        self.receiver.switch_off(self.text)

    def undo(self):
        self.receiver.switch_on(f'Undoing: {self.text}')


# Invoker
class Invoker(object):
    def __init__(self):
        self.commands = []
        self.undo_commands = []

    def add_command(self, command: Command):
        self.commands.append(command)

    def run(self):
        for command in self.commands:
            command.execute()
            self.undo_commands.append(command)

    def undo(self):
        undo_command = self.undo_commands.pop()
        undo_command.undo()


if __name__ == '__main__':
    switch = Switch()
    invoker = Invoker()

    switch_on_command = SwitchOnCommand(receiver=switch, text="Switch On")
    switch_off_command = SwitchOffCommand(receiver=switch, text="Switch Off")

    invoker.add_command(command=switch_on_command)
    invoker.add_command(command=switch_off_command)

    invoker.run()

    invoker.undo()
    invoker.undo()
