"""
Instead of creating products(instances) directly from the units(classes), ask factory (factory method) to create
the products(instances)
"""
from enum import Enum


class MachineType(Enum):
    MachineA = 1
    MachineB = 2


# Factory Method
def factory(type: MachineType, level: int):
    if type == MachineType.MachineA:
        return MachineA(level)
    elif type == MachineType.MachineB:
        return MachineB(level)
    else:
        assert 0, 'Invalid Machine Type'


# Machines Unit
class MachineA(object):
    def __init__(self, level):
        print(f'Creating Machine A with level {level}')

    def work(self):
        print('Machine A is wokring')


class MachineB(object):
    def __init__(self, level):
        print(f'Creating Machine B with level {level}')

    def work(self):
        print('Machine B is working')


if __name__ == '__main__':
    resources = [
        factory(MachineType.MachineA, level=2),
        factory(MachineType.MachineB, level=4)
    ]

    for resource in resources:
        resource.work()
