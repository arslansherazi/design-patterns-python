"""
Chain of responsibility pattern is used to achieve loose coupling in software design where a request from the client is
passed to a chain of objects to process them. Later, the object in the chain will decide themselves who will be
processing the request and whether the request is required to be sent to the next object in the chain or not.
"""
from abc import ABCMeta, abstractmethod


class Logger(metaclass=ABCMeta):
    def __init__(self, logging_message: str):
        self.logging_message = logging_message
        self.next = None

    def set_next(self, next_fn):
        self.next = next_fn

    @abstractmethod
    def handler(self):
        pass

    def execute(self):
        self.handler()
        if self.next:
            self.next.execute()


class FileLogger(Logger):
    def handler(self):
        print(f'This is file logger: {self.logging_message}')


class ServerLogger(Logger):
    def handler(self):
        print(f'This is server logger: {self.logging_message}')


class ScreenLogger(Logger):
    def handler(self):
        print(f'This is screen logger: {self.logging_message}')


class AlarmLogger(Logger):
    def handler(self):
        print(f'This is alarm logger: {self.logging_message}')


if __name__ == '__main__':
    message = 'This is logging message'
    filer_logger = FileLogger(message)
    server_logger = ServerLogger(message)
    screen_logger = ScreenLogger(message)
    alarm_logger = AlarmLogger(message)

    filer_logger.next = server_logger
    server_logger.next = screen_logger
    screen_logger.next = alarm_logger

    filer_logger.execute()