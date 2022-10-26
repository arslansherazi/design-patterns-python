"""
- Visitor design pattern is one of the behavioral design patterns. It is used when we have to perform an operation on a
  group of similar kind of Objects. With the help of visitor pattern, we can move the operational logic from the objects
  to another class.
- The visitor pattern consists of two parts:
    1. a method called Visit() which is implemented by the visitor and is called for every element in the data structure
    2. visitable classes providing Accept() methods that accept a visitor
"""
from abc import ABCMeta, abstractmethod


# Visitable
class Item(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class Book(Item):
    def __init__(self, book_id: str, price: int):
        self.book_id = book_id
        self.price = price

    def accept(self, visitor):
        return visitor.visit(self)


class Fruit(Item):
    def __init__(self, name: str, price_per_kg: int, weight: int):
        self.name = name
        self.price_per_kg = price_per_kg
        self.weight = weight

    def accept(self, visitor):
        return visitor.visit(self)


# Visitor
class Visitor(metaclass=ABCMeta):
    def visit(self, item: Item):
        pass


class ShoppingCartVisitor(Visitor):
    def visit(self, item: Item):
        print(item.__dict__)


if __name__ == '__main__':
    book = Book(book_id='ENG349', price=2000)
    fruit = Fruit(name='Mango', price_per_kg=200, weight=10)

    book.accept(visitor=ShoppingCartVisitor())
    fruit.accept(visitor=ShoppingCartVisitor())
