"""
State design pattern is used when an Object changes its behavior based on its internal state.
"""
from abc import ABCMeta, abstractmethod


class MobileAlertState(metaclass=ABCMeta):
    @abstractmethod
    def alert(self):
        pass


class Vibration(MobileAlertState):
    def alert(self):
        print('Mobile is vibrating')


class Silent(MobileAlertState):
    def alert(self):
        print('Mobile is silent')


class AlertState(object):
    def __init__(self):
        self.current_state = Vibration()

    def set_state(self, state: MobileAlertState):
        self.current_state = state

    def alert(self):
        self.current_state.alert()


if __name__ == '__main__':
    alert_state = AlertState()

    alert_state.alert()
    alert_state.alert()

    alert_state.set_state(state=Silent())

    alert_state.alert()
    alert_state.alert()
