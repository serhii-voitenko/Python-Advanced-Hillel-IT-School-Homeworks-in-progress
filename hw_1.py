"""
1) Сгенерировать dict() из списка ключей ниже по формуле (key : key*key).

 keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 ожидаемый результат: {1: 1, 2: 4, 3: 9 …} 
"""

keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print({k: k * k for k in keys})

"""
2) Сгенерировать массив(list()). Из диапазона чисел от 0 до 100 записать в результирующий массив только четные числа. 
"""

print([i for i in range(101) if i % 2 == 0])

"""
3)Заменить в произвольной строке согласные буквы на гласные.  
"""

import random


def consonants_to_vowels(some_string):
    vowels = 'aeiouAEIOU'
    for letter in some_string:
        for vowel in vowels:
            if letter.isalpha() and letter not in vowels:
                some_string = some_string.replace(letter, random.choice(vowels))
    print(f'Encoded: {some_string}')


consonants_to_vowels(str(input('print something to encode: ')))

"""
4)Дан массив чисел. [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]  
4.1) убрать из него повторяющиеся элементы 
4.2) вывести 3 наибольших числа из исходного массива  
4.3) вывести индекс минимального элемента массива
4.4) вывести исходный массив в обратном порядке 
"""

ARRAY = [10, 11, 2, 3, 5, 8, 23, 11, 2, 5, 76, 43, 2, 32, 76, 3, 10, 0, 1]


def repetitions_removal():
    copy_list = ARRAY.copy()
    for item in copy_list:
        if copy_list.count(item) > 1:
            copy_list.remove(item)
    print(f'Repetitions removed: {copy_list}')


def greatest_numbers():
    copy_list = ARRAY.copy()
    copy_list.sort(reverse=True)
    print(f'Three greatest numbers: {copy_list[0:3]}')


def min_key():
    copy_list = ARRAY.copy()
    print(f'Min value: {min(copy_list)}. Its index is - {copy_list.index(0)}')


def reverse_list():
    copy_list = ARRAY.copy()
    copy_list.reverse()
    print(f'Reversed array: {copy_list}')


repetitions_removal()
greatest_numbers()
min_key()
reverse_list()

"""
5) Найти общие ключи в двух словарях: 
dict_one = { ‘a’: 1,  ‘b’: 2, ‘c’: 3,  ‘d’: 4 }
  dict_two = { ‘a’: 6,  ‘b’: 7, ‘z’: 20,  ‘x’: 40 } 
"""

dict_one = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict_two = {'a': 6, 'b': 7, 'z': 20, 'x': 40}
generic_keys = []

for key in dict_one:
    if key in dict_two.keys():
        generic_keys.append(key)
print(f'Generic keys are: {generic_keys}')

