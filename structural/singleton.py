# Singleton using function of class
class Singleton(object):
    __instance = None  # private data member

    def __init__(self):
        raise Exception('This is singleton class')

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = cls.__new__(cls)
        return cls.__instance

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


# Singleton using Inner Class
class Singleton1(object):
    class __Singleton(object):
        def __init__(self):
            self.value = None

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = Singleton1.__Singleton()
        return cls.__instance

    def __setattr__(self, key, value):
        return setattr(self.__instance, key, value)

    def __getattr__(self, item):
        return getattr(self.__instance, item)

    def __str__(self):  # invokes when object is printed
        return str(self.__instance)


if __name__ == '__main__':
    print('################# Singleton using Function of Class #################')
    try:
        s = Singleton()
    except Exception:
        print('Error creating instance')

    s1 = Singleton.get_instance()
    s1.set_value(100)

    s2 = Singleton.get_instance()

    print(s1.get_value())
    print(s2.get_value())

    print('################# Singleton using Inner Class #################')
    s1 = Singleton1()
    s2 = Singleton1()
    s1.value = 200
    print(s1, s1.value)
    print(s1, s2.value)
