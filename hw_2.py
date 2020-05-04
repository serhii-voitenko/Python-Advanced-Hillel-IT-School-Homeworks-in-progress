# 1)Дан массив из словарей 

data = [
    {'name': 'Viktor', 'city': 'Kiev', 'age': 30},
    {'name': 'Maksim', 'city': 'Dnepr', 'age': 20},
    {'name': 'Vladimir', 'city': 'Lviv', 'age': 32},
    {'name': 'Andrey', 'city': 'Kiev', 'age': 34},
    {'name': 'Artem', 'city': 'Dnepr', 'age': 50},
    {'name': 'Dmitriy', 'city': 'Lviv', 'age': 21}]

# 1.1) отсортировать массив из словарей по значению ключа ‘age' 

data.sort(key=lambda age: age['age'])
print(data)

# 1.2) сгруппировать данные по значению ключа 'city' 
# вывод должен быть такого вида :

"""result = {
   'Kiev': [
      {'name': 'Viktor', 'age': 30 },
      {'name': 'Andrey', 'age': 34}],

   'Dnepr': [ {'name': 'Maksim', 'age': 20 },
              {'name': 'Artem', 'age': 50}],
   'Lviv': [ {'name': 'Vladimir', 'age': 32 },
             {'name': 'Dmitriy', 'age': 21}]
}
"""

result = {}
Kyev_data = []
Dnepr_data = []
Lviv_data = []
for element in data:
    for key, value in element.items():
        if key == 'city':
            if value == 'Kiev':
                Kyev_data.append({k: element[k] for k in element.keys() - {'city'}})
                result.update({value: Kyev_data})
            elif value == 'Dnepr':
                Dnepr_data.append({k: element[k] for k in element.keys() - {'city'}})
                result.update({value: Dnepr_data})
            else:
                Lviv_data.append({k: element[k] for k in element.keys() - {'city'}})
                result.update({value: Lviv_data})

print(result)

# =======================================================

# 2) У вас есть последовательность строк. Необходимо определить наиболее часто встречающуюся строку в последовательности.
# Например:

import statistics


def most_frequent(list_var):
    print(statistics.mode(list_var))


most_frequent(['a', 'a', 'bi', 'bi', 'bi'])

# =======================================================

# 3) Дано целое число. Необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.
# Например:
# Дано число 123405. Результат будет: 1*2*3*4*5=120.

from functools import reduce

numbers = 123405
numbers_list = list(map(int, str(numbers)))
print(reduce((lambda x, y: x * y), filter(None, numbers_list)))


# =======================================================
# 4) Есть массив с положительными числами и число n (def some_function(array, n)).
# Необходимо найти n-ую степень элемента в массиве с индексом n. Если n за границами массива, тогда вернуть -1.

def some_function(array, n):
    if n in range(array[0], array[-1]):
        return array[n]**n
    return -1
print(some_function([1, 3, 4, 10, 14], 3))

# =======================================================
# 5) Есть строка со словами и числами, разделенными пробелами (один пробел между словами и/или числами).
# Слова состоят только из букв. Вам нужно проверить есть ли в исходной строке три слова подряд.
# Для примера, в строке "hello 1 one two three 15 world" есть три слова подряд.

import re

some_string = "hello 1 one two three 15 world"
match = re.findall(r"\D+\s\D+\s\D+", some_string)
print('3 words are exists' if match else '3 words are not found')
