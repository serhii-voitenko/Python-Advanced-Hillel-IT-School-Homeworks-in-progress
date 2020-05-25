"""Task1
Take a string with a couple words and returns the length of the longest word.
"""

print(max(len(word) for word in 'I was running'.split()))

"""Task2
Change a given string to a new string where the first and last chars have been exchanged.
"""


def change_string(str1):
    # str = str1.replace(str1[0], str1[-1])
    # str2 = str1.replace(str1[1:-1], str1)
    # return str.replace(str[1:], str1[1:])


print(change_string('abcd'))  # dbcd
print(change_string('12345'))  # 52341


"""Task3
Sum all the items in a given list
"""

print(sum([3, 4, 2, 10]))

"""Task4
Return the largest number from a list
"""

print(max([3, 4, 2, 10]))

"""Task5
Return the smallest number from a list
"""

print(min([3, 4, 2, 10]))


"""Taks6
Take two lists and returns True if they have at least one common member
"""

list1 = [-3, 0, 100, 6, 98]
list2 = [-5, 1, 10, 6, 90]
print(any(x in list2 for x in list1))


"""Task7
Map two lists into a dictionary.
keys = ['red', 'green', 'blue']
values = ['#FF0000', '#008000', '#0000FF']
"""

keys = ['red', 'green', 'blue']
values = ['#FF0000', '#008000', '#0000FF']
print(dict.fromkeys(keys, values))

"""Task8
Convert a tuple to a string.
tuple = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
"""

tuple = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
string = ''
print(string.join(tuple))

"""Task9
Unpack a tuple in several variables.
"""
_
