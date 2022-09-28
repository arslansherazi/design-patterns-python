"""
Instead of creating instances of classes from scratch, define different prototypes of possible instances
"""
from abc import ABCMeta, abstractmethod
from copy import deepcopy


class PrototypeRepo(object):
    def __init__(self):
        self.prototypes = {
            'MachineA': {
                1: MachineA(1),
                2: MachineA(2),
                3: MachineA(3)
            },
            'MachineB': {
                1: MachineB(1),
                2: MachineB(2)
            }
        }

    def create_machine(self, machine_type, level):
        return self.prototypes[machine_type][level]


class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def clone(self):
        pass


class MachineA(Prototype):
    def __init__(self, level):
        if level == 1:
            self.attribute1 = 100
            self.attribute2 = 200
            self.attribute3 = 300
        elif level == 2:
            self.attribute1 = 1000
            self.attribute2 = 2000
            self.attribute3 = 3000

    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return f'{self.attribute1}\t{self.attribute2}\t{self.attribute3}'


class MachineB(Prototype):
    def __init__(self, level):
        if level == 1:
            self.attribute1 = 891
            self.attribute2 = 672
        elif level == 2:
            self.attribute1 = 901
            self.attribute2 = 903

    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return f'{self.attribute1}\t{self.attribute2}'


if __name__ == '__main__':
    prototype_repo = PrototypeRepo()
    machine_a = prototype_repo.create_machine(machine_type='MachineA', level=2)
    machine_b = prototype_repo.create_machine(machine_type='MachineB', level=1)
    print(machine_a)
    print(machine_b)
