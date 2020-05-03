"""Есть таблица продуктов на складе. Данные представлены в виде list of dicts
Найти самые дорогие товары. Количество товаров, которые необходимо вывести будет передано в первом аргументе, данные по
товарам будут переданы вторым аргументом.
bigger_price(2, [
{"name": "bread", "price": 100},
{"name": "wine", "price": 138},
{"name": "meat", "price": 15},
{"name": "water", "price": 1}
]) == [
{"name": "wine", "price": 138},
{"name": "bread", "price": 100}
]
"""


def bigger_price(count, list):
    for item in list:
        for elem in item.items():
            if v == max(v):
                return item.items()


print(bigger_price(2, [
{"name": "bread", "price": 100},
{"name": "wine", "price": 138},
{"name": "meat", "price": 15},
{"name": "water", "price": 1}
]))

"""
Есть адрес https://lego-super-heroes.herokuapp.com/ 
От меня Все: (01:38 PM)
Вам необходимо собрать все имена героев в лист и вернуть его Собрать имена всех героев и их оружие и вернуть в виде {name: weapon} только для тех у кого есть оружие """
