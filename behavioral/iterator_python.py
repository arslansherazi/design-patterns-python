"""
- Python has builtin magic functions for iteration of aggregated objects
"""
from abc import ABCMeta, abstractmethod


# Iterator
class MyList(object):
    def __init__(self, *args):
        self.list = list(args)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.list):
            self.index += 1
            return self.list[self.index - 1]
        else:
            raise StopIteration()


if __name__ == '__main__':
    m_list = MyList(1, 2, 3, 4, 5)

    for element in m_list:
        print(element)

    # equivalent of above traversing but did not work as we already traverse the list and index of list = len of list
    while True:
        try:
            print(m_list.__next__())
        except StopIteration:
            break
