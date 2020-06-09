"""Из текстового файла удалить все слова, содержащие от трех до пяти символов, но при этом из каждой строки должно быть
удалено только четное количество таких слов.
"""
import re
import pandas as pd
import datetime


class WordParsing(object):
    """Class for opening text file and delete certain words."""

    def __init__(self, file_to_open):
        self._file_to_open = file_to_open
        self._oper_string = ''

    def open_file(self):
        """Method to read from existing file."""
        with open(self._file_to_open, 'r') as file_to_read:
            self._oper_string = file_to_read.read()
            return self._oper_string

    def write_to_file(self):
        """This method creates a new text file and write changed text to it."""
        with open('hw_5_1_new.txt', 'w') as file_to_write:
            file_to_write.write(self._oper_string)

    def main(self):
        """Main class method. """
        self.open_file()
        for line in self._oper_string.splitlines():
            for word in line.split():
                if 3 <= len(word) <= 5:
                    if self._oper_string.splitlines().count(word) % 2 == 0:
                        self._oper_string = self._oper_string.replace(word, '')
        self.write_to_file()


word_parsing = WordParsing('hw_5_1.txt')
# word_parsing.main()


"""Текстовый файл содержит записи о телефонах и их владельцах. Переписать в другой файл телефоны тех владельцев,
фамилии которых начинаются с букв К и С.
Получить файл g, в котором текст выровнен по правому краю путем равномерного добавления пробелов.
"""


class PhoneBook(object):
    """Class for finding special abonents in list"""

    def __init__(self, file_to_open):
        self._file_to_open = file_to_open
        self._k_c_list = []
        self._get_string = ''
        self._formatted_string = ''

    def open_file(self):
        """This method opens a file."""
        with open(self._file_to_open, 'r') as file_to_read:
            self._get_string = file_to_read.read()
        return self._get_string

    def search_for_special_abonents(self):
        """This method searches for abonents who's lastname starts with "K" or "C"."""
        for abonent in self._get_string.splitlines():
            if re.search(r'.+\s\w+\s[K,C]', abonent):
                self._k_c_list.append(abonent)
        return self._k_c_list

    def format_the_text_to_the_right_side(self):
        """This method return the text right aligned."""
        self._formatted_string = '\n'.join(self._k_c_list)
        for line in self._formatted_string.splitlines():
            self._formatted_string = self._formatted_string.replace(line, line.rjust(100))
        return self._formatted_string

    def get_new_file(self):
        """This method save the info to the new file."""
        with open('g', 'w') as file_to_write:
            file_to_write.write(self._formatted_string)

    def main(self):
        """The main class method."""
        self.open_file()
        self.search_for_special_abonents()
        self.format_the_text_to_the_right_side()
        self.get_new_file()


phone_book_searching = PhoneBook('hw_5_2.txt')
# phone_book_searching.main()

"""Дан текстовый файл со статистикой посещения сайта за неделю. Каждая строка содержит ip адрес,
время и название дня недели (например, 139.18.150.126  23:12:44  sunday). Создайте новый текстовый файл,
который бы содержал список ip без повторений из первого файла. Для каждого ip укажите количество посещений,
наиболее популярный день недели, наиболее популярный отрезок времени длиной в один час. Последней строкой в файле
добавьте наиболее популярный отрезок времени в сутках длиной один час в целом для сайта.
"""


class SiteVisitStatistics(object):
    """This class for working with site visiting statistics txt file. It can collect Ip addresses, time of visits and
    days of week, when users entered this web site and makes a table with time when were more often visits and day of
    the week.
    """

    def __init__(self, file_to_open):
        self._file_to_open = file_to_open

    def main(self):
        """Method to open the text file with using pandas."""
        getting_data = pd.read_csv('hw_5_3.txt', delim_whitespace=True, names=['IP', 'Time', 'Day_of_the_week'])
        print(getting_data)
        print(getting_data['IP'].value_counts())
        print(getting_data['Time'].value_counts())

    # def write_to_file(self):
    #     """Method to write new data to the new text file."""
    #     with open('hw_5_3_new.txt', 'w') as file_to_write:
    #         file_to_write.write()


site_stat = SiteVisitStatistics('hw_5_3.txt')
site_stat.main()
