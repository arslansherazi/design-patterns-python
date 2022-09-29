"""
Instead of creating products(instances) directly from the machines/units(classes), ask factory(factory class) to create the product(instance)
"""
from abc import ABCMeta, abstractmethod
from enum import Enum


class MachineType(Enum):
    MachineA = 1
    MachineB = 2


class ProductType(Enum):
    ProductA = 1
    ProductB = 2


# Abstract factory
class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_object(self, type, level):
        pass


# Machine Factory
class MachineFactory(AbstractFactory):
    def create_object(self, type, level):
        if type == MachineType.MachineA:
            return MachineA(level)
        elif type == MachineType.MachineB:
            return MachineB(level)
        else:
            assert 0, 'Invalid Machine Type'


# Product Factory
class ProductFactory(AbstractFactory):
    def create_object(self, type, level):
        if type == ProductType.ProductA:
            return ProductA(level)
        elif type == ProductType.ProductB:
            return ProductB(level)
        else:
            assert 0, 'Invalid Product Type'


# Machines Unit
class Machine(metaclass=ABCMeta):
    @abstractmethod
    def work(self):
        pass


class MachineA(Machine):
    def __init__(self, level):
        print(f'Creating Machine A with level {level}')

    def work(self):
        print('Machine A is wokring')


class MachineB(Machine):
    def __init__(self, level):
        print(f'Creating Machine B with level {level}')

    def work(self):
        print('Machine B is working')


# Products Unit
class Product(metaclass=ABCMeta):
    @abstractmethod
    def work(self):
        pass


class ProductA(Product):
    def __init__(self, level):
        print(f'Creating Product A with level {level}')

    def work(self):
        print('Product A is wokring')


class ProductB(Product):
    def __init__(self, level):
        print(f'Creating Product B with level {level}')

    def work(self):
        print('Product B is working')


if __name__ == '__main__':
    machine_factory = MachineFactory()
    product_factory = ProductFactory()

    resources = [
        machine_factory.create_object(MachineType.MachineA, level=2),
        machine_factory.create_object(MachineType.MachineB, level=4),
        product_factory.create_object(ProductType.ProductA, level=10),
        product_factory.create_object(ProductType.ProductB, level=20)
    ]

    for resource in resources:
        resource.work()
