"""
When we have large no of attributes in a class then we use Builder pattern to create the instance instead of creating
by using constructor to avoid passing of attribute values to the constructor as arguments

Architecture:
    User(asks director to build the product) --> Director(builds the product by using builder) --> Builder(Actually builds the product) --> Product

- When not to use builder pattern
    When we have small no of attributes in a class
"""
from abc import ABCMeta, abstractmethod


class House(object):
    def __init__(self):
        self.type = None
        self.foundation = None
        self.walls = None
        self.roofs = None
        self.doors = None
        self. windows = None

    def __str__(self):
        return f'''
            type: {self.type}\n 
            foundation: {self.foundation}\n 
            walls: {self.walls}\n 
            roofs: {self.roofs}\n
        '''


class Builder(metaclass=ABCMeta):
    def __init__(self, constructed_object):
        self.constructed_object = constructed_object

    @abstractmethod
    def set_type(self):
        pass

    @abstractmethod
    def build_foundation(self):
        pass

    @abstractmethod
    def build_walls(self):
        pass

    @abstractmethod
    def build_roofs(self):
        pass


class HouseBuilder(Builder):
    def __init__(self):
        super().__init__(constructed_object=House())

    def set_type(self):
        self.constructed_object.type = 'Villa'

    def build_foundation(self):
        self.constructed_object.foundation = 'Concrete'

    def build_walls(self):
        self.constructed_object.walls = []
        for i in range(10):
            self.constructed_object.walls.append(f'Wall: {i+1}')

    def build_roofs(self):
        self.constructed_object.roofs = []
        for i in range(10):
            self.constructed_object.roofs.append(f'Roof: {i+1}')


class Director(metaclass=ABCMeta):
    def __init__(self):
        self._builder = None

    def set_builder(self, builder):
        self._builder = builder

    @abstractmethod
    def construct(self):
        pass

    def get_constructed_object(self):
        return self._builder.constructed_object


class HouseDirector(Director):
    def __init__(self):
        super().__init__()

    def construct(self):
        self._builder.set_type()
        self._builder.build_foundation()
        self._builder.build_walls()
        self._builder.build_roofs()


if __name__ == '__main__':
    builder = HouseBuilder()
    director = HouseDirector()
    director.set_builder(builder)

    director.construct()
    house = director.get_constructed_object()
    print(house)
