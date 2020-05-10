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
cache = {}
counter = 0


def check_module(func_to_decorate):
    """Check the remnant of division 100 to func. """
    def wrapper(number):
        func_to_decorate(number)
        if 100 % func_to_decorate(number) == 0:
            print('We are OK!')
        else:
            print(f'Bad news guys, we got {100 % func_to_decorate(number)}')
        return func_to_decorate(number)
    return wrapper


def check_type_integer(func_to_decorate):
    """Checking the income variable for type and raise the errors. """
    def wrapper(number):
        if type(number) is int:
            return func_to_decorate(number)
        elif type(number) is str:
            raise ValueError('String type is not supported')
        else:
            raise TypeError('Are you seriously?')
    return wrapper


def caching_the_func(func_to_decorate):
    """Cache the arguments of the function and results. Show the frequency of work the function. """
    def wrapper(number):
        global cache, counter
        if number in cache:
            counter += 1
            print(f'Used cache with counter = {counter}')
            return cache[number]
        else:
            cache[number] = func_to_decorate(number)
            counter += 1
            print(f'Function executed with counter = {counter}, function result = {cache[number]}')
            return cache[number]
    return wrapper


@caching_the_func
@check_module
@check_type_integer
def main(number):
    """Main function increment. """
    return number + 1


main(1)
main(2)
main(34)
main(10)
main(2)





