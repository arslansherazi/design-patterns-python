"""
- Used for aggregate objects (objects containing multiple elements like lined list)
"""
from abc import ABCMeta, abstractmethod


# Iterator
class Iterator(metaclass=ABCMeta):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass


class MyListIterator(Iterator):
    def __init__(self, source):
        self.my_list = source.list
        self.current_index = 0

    def has_next(self):
        return self.current_index < len(self.my_list)

    def next(self):
        self.current_index += 1
        return self.my_list[self.current_index - 1]


#  Container
class Container(metaclass=ABCMeta):
    @abstractmethod
    def get_iterator(self):
        pass


class MyList(Container):
    def __init__(self, *args):
        self.list = list(args)

    def get_iterator(self):
        return MyListIterator(source=self)


if __name__ == '__main__':
    m_list = MyList(1, 2, 3, 4, 5)
    m_iter = m_list.get_iterator()

    while m_iter.has_next():
        print(m_iter.next())
