# ______________________________ 1 _____________________________


def my_decor_uppercase(func):
    def wrapper(*args):
        func(*args)
        return print(func(*args).upper())
    return wrapper


@my_decor_uppercase
def main(name, lastname):
    return name + lastname


main('steven ', 'spielberg')


# ______________________________ 2 _____________________________

def supress_exception(error_to_raise):
    def work_with_func(func):
        def wrapper(a):
            try:
                func(a)
                print(f'{func.__name__} works well')
            except error_to_raise:
                print(f'{error_to_raise.__name__} was catched')
        return wrapper
    return work_with_func


@supress_exception(KeyError)
def main2(a):
    random_dict = {}
    return random_dict[a]


main2(5)


# _____________________________ 3 _____________________________
"""
Написать декоратор с параметром который считает время выполнения вашей функции. 
Внутри декоратора объявить функцию clear_file_log() которая будет очищать файл. 
В качестве аргумента декоратору передать имя файла в который сохраняются данные (имя функции - результат работы - время)
"""
import math
from datetime import datetime


def counter_log(file):
    def work_with_func(func):
        def wrapper(a):
            start = datetime.now()
            func(a)
            with open(file, 'a+') as log_file:
                log_file.write(f'\nfunction {func.__name__} with variable {a}, \nworks {datetime.now() - start}\n')

        def clear_file_log():
            with open(file, 'w') as log_file:
                log_file.write('')

        wrapper.clear = clear_file_log

        return wrapper
    return work_with_func


@counter_log('time_log.txt')
def main3(a):
    return math.factorial(a)


main3(3)
main3(4)
main3(5)
main3(6)
main3.clear()
main3(0)

