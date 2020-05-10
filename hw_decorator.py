# ЗАДАЧА-1
# Написать свой декоратор который будет проверять остаток от деления числа 100 на результат работы функции ниже.
# Если остаток от деления = 0, вывести сообщение "We are OK!», иначе «Bad news guys, we got {}» остаток от деления.

# ЗАДАЧА-2
# Написать декоратор который будет выполнять предпроверку типа аргумента который передается в вашу функцию.
# Если это int, тогда выполнить функцию и вывести результат, если это str(),
# тогда зарейзить ошибку ValueError (raise ValueError(“string type is not supported”))

# ЗАДАЧА-3
# Написать декоратор который будет кешировать значения аргументов и результаты работы вашей функции и записывать
# его в переменную cache. Если аргумента нет в переменной cache и функция выполняется, вывести сообщение
# «Function executed with counter = {}, function result = {}» и количество раз сколько эта функция выполнялась.
# Если значение берется из переменной cache, вывести сообщение «Used cache with counter = {}» и
# количество раз обращений в cache.


def check_module(func_to_decorate):
    def wrapper(number):
        func_to_decorate(number)
        if 100 % func_to_decorate(number) == 0:
            print('We are OK!')
        print(f'Bad news guys, we got {100 % func_to_decorate}')
    return wrapper


def check_type_integer(func_to_decorate):
    def wrapper(number):
        try:
            type(number) is int
        except number is str:
            raise ValueError('String type is not supported')
        func_to_decorate(number)

    return wrapper


@check_module
@check_type_integer
def main(number):
    return number + 1


print(main(1))

