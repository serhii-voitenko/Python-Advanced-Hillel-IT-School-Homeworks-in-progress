import os
from contextlib import suppress, ContextDecorator
from datetime import datetime

"""Задача-1
Создать объект менеджера контекста который будет переходить в папку которую он принимает на вход.
Так же ваш объект должен принимать исключение которое он будет подавлять.
Если флаг об исключении отсутствует, исключение должно быть поднято.
"""


class CD(object):
    """Class context manager which opens a directory and suppress subsequent exceptions which we can add."""
    def __init__(self, path, *my_exceptions):
        """Takes in
        path: needed directory and,
        my_exceptions: tuple of exceptions which we can to crush.
        """
        self.path = path
        self.my_exc = my_exceptions
        self.saved_cwd = None

    def __enter__(self):
        """Remember the current dir and go to needed dir. """
        self.saved_cwd = os.getcwd()
        return os.chdir(self.path)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """We determine type of basic exception which we need to crush."""
        os.chdir(self.saved_cwd)
        exc_type = PermissionError
        return exc_type is not None and issubclass(exc_type, self.my_exc)


with CD("/home/serhii/", OSError) as go_to_path:
    os.mkdir("/home/serhii/test", mode=0o755)


"""Задача -2
Описать задачу выше но уже с использованием @contextmanager
"""

with suppress(OSError):
    os.mkdir("/home/serhii/test", mode=0o755)


"""Задача -3
Создать менеджер контекста который будет подсчитывать время выполнения вашей функции.
"""


class MyTimer(ContextDecorator):
    """Custom class context manager which can work as a decorator. It can count time of working function."""
    def __enter__(self):
        self.start_time = datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('The time of executing is: {}'.format(datetime.now() - self.start_time))


@MyTimer()
def some_func():
    return 100*100


print(some_func())
