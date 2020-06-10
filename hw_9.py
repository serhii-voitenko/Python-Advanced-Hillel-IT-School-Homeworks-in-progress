import re
from typing import Optional

# Задача-1
# Реализовать дескриптор валидации для аттрибута email.
# Ваш дескриптор должен проверять формат email который вы пытаетесь назначить


class EmailDescriptor:
    """Descriptor which manage the email validation. """
    def __init__(self):
        self._email = None

    def __get__(self, instance, owner):
        return self._email

    def __set__(self, instance, value):
        """Execute the procedure of matching setted email to pattern."""
        if not re.findall(r'^[a-z0-9._%+-]+@[a-z0-9.-]+.[a-z]{2,6}$', value):
            raise AttributeError('Your email is not valid. Please enter the correct email.')
        else:
            self._email = value


class MyClass:
    email = EmailDescriptor()


my_class = MyClass()
my_class.email = "validemail@gmail.com"

# my_class.email = "novalidemail"


# Задача-2
# Реализовать синглтон метакласс(класс для создания классов синглтонов).

class Singleton(type):
    _instance: Optional[MyClass] = None

    def __call__(cls, *args, **kwargs) -> MyClass:
        if cls._instance is None:
            cls._instance = super().__call__()
        return cls._instance


class MyClass(metaclass=Singleton):
    pass


c = MyClass()
b = MyClass()
assert id(c) == id(b)


# Задача-3
# реализовать дескриптор IngegerField(), который будет хранить уникальные
# состояния для каждого класса где он объявлен

class IngegerField:
    """Descriptor for saving unique variables for different instances without rewriting."""
    def __init__(self):
        self.number = None

    def __get__(self, instance, owner):
        return self.__dict__[instance]

    def __set__(self, instance, value):
        """Adding a new key-value pair to the class attributes."""
        if value != self.number:
            self.number = self.__dict__.update({instance: value})


class Data:
    number = IngegerField()


data_row = Data()
new_data_row = Data()

data_row.number = 5
new_data_row.number = 10

assert data_row.number != new_data_row.number

