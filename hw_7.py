import json
import os

"""Задача-1
У вас есть список(list) IP адрессов. Вам необходимо создать
класс который будет иметь методы:
1) Получить список IP адресов
2) Получить список IP адресов в развернутом виде
(10.11.12.13 -> 13.12.11.10)
3) Получить список IP адресов без первых октетов
(10.11.12.13 -> 11.12.13)
4) Получить список последних октетов IP адресов
(10.11.12.13 -> 13)
"""


class IPShow(object):
    """Class to show different varieties of Ip list."""
    def __init__(self):
        self.__IP_list = ['135.146.235.135', '38.100.72.185', '127.27.201.98', '236.144.28.224', '57.80.195.145',
                          '152.212.218.100', '219.20.3.53', '79.112.140.199', '33.98.75.82', '165.230.55.81',
                          '236.78.64.193', '255.113.161.134', '116.70.239.18', '254.110.243.118', '226.241.61.154']

    @property
    def ip_list_getting(self):
        """Method to get private Ip list."""
        return self.__IP_list

    @property
    def reversed_ip_list(self):
        """Method to get Ip list in reversed view."""
        new_list = []
        for elem in self.__IP_list:
            new_list.append('.'.join(elem.split('.')[::-1]))
        return new_list

    @property
    def ip_list_without_first_octets(self):
        """Method to get IP list without first octets."""
        new_list = []
        for elem in self.__IP_list:
            new_list.append('.'.join(elem.split('.')[1:]))
        return new_list

    @property
    def ip_list_last_octets(self):
        """Method to get last octets of existing IP list."""
        new_list = []
        for elem in self.__IP_list:
            new_list.append('.'.join(elem.split('.')[3:]))
        return new_list


task1 = IPShow()
print(task1.ip_list_getting)
print(task1.reversed_ip_list)
print(task1.ip_list_without_first_octets)
print(task1.ip_list_last_octets)

"""Задача-2
У вас несколько JSON файлов. В каждом из этих файлов есть
произвольная структура данных. Вам необходимо написать
класс который будет описывать работу с этими файлами, а
именно:
1) Запись в файл
2) Чтение из файла
3) Объединение данных из файлов в новый файл
4) Получить относительный путь к файлу
5) Получить абсолютный путь к файлу
"""


class JsonWork(object):
    """Class which has methods to work with json files."""
    def record_to_json_file(self, file_to_write, data_to_write):
        """Method for writing the data to json file."""
        with open(file_to_write, 'w') as json_file:
            json.dump(data_to_write, json_file, indent=2)

    def read_from_json_file(self, file_to_read):
        """Method for reading from the json file."""
        with open(file_to_read, 'r') as json_file:
            data_from_json = json.load(json_file)
            print(data_from_json)

    def union_data_from_json_files_to_new_json_file(self, file_to_union_1, file_to_union_2, new_json_file):
        """Method which makes a new json data file from exiting ones."""
        with open(file_to_union_1, 'r') as json_file_1:
            data_from_json_1 = json.load(json_file_1)
        with open(file_to_union_2, 'r') as json_file_2:
            data_from_json_2 = json.load(json_file_2)
        with open(new_json_file, 'w') as json_file_new:
            json.dump((data_from_json_1, data_from_json_2), json_file_new, indent=2)

    def relative_path_to_file(self, some_file):
        """Method shows the relative path to the file."""
        print(os.path.normpath(some_file))

    def absolute_path_to_file(self, some_file):
        """Method shows the absolute path to the file."""
        print(os.path.abspath(some_file))


task2 = JsonWork()
task2.record_to_json_file('hw_7_json1.json', {'name': 'User1', 'phone': '80999999999', 'email': 'www@gmail.com'})
task2.record_to_json_file('hw_7_json2.json', {'name': 'User2', 'phone': '80888888888', 'email': 'aaa@gmail.com'})
task2.read_from_json_file('hw_7_json1.json')
task2.read_from_json_file('hw_7_json2.json')
task2.union_data_from_json_files_to_new_json_file('hw_7_json1.json', 'hw_7_json2.json', 'hw_7_new_json_file.json')
task2.read_from_json_file('hw_7_new_json_file.json')
task2.relative_path_to_file('hw_7_new_json_file.json')
task2.absolute_path_to_file('hw_7_new_json_file.json')


"""Задача-3
Создайте класс который будет хранить параметры для
подключения к физическому юниту(например switch). В своем
списке атрибутов он должен иметь минимальный набор
(unit_name, mac_address, ip_address, login, password).
Вы должны описать каждый из этих атрибутов в виде гетеров и
сеттеров(@property). У вас должна быть возможность
получения и назначения этих атрибутов в классе.
"""


class SwitchParameters(object):
    """Class which can manage the switch attributes."""

    def __init__(self, unit_name, mac_address, ip_address, login, password):
        self.__unit_name = unit_name
        self.__mac_address = mac_address
        self.__ip_address = ip_address
        self.__login = login
        self.__password = password

    @property
    def unit_name(self):
        """Show unit name."""
        return self.__unit_name

    @property
    def mac_address(self):
        """Show mac address."""
        return self.__mac_address

    @property
    def ip_address(self):
        """Show ip address."""
        return self.__ip_address

    @property
    def login(self):
        """Show user login."""
        return self.__login

    @property
    def password(self):
        """Show user password."""
        return self.__password

    @unit_name.setter
    def unit_name(self, new_unit_name):
        """Set a new unit name."""
        self.__unit_name = new_unit_name

    @mac_address.setter
    def mac_address(self, new_mac_address):
        """Set a new mac address."""
        self.__mac_address = new_mac_address

    @ip_address.setter
    def ip_address(self, new_ip_address):
        """Set a new ip address."""
        self.__ip_address = new_ip_address

    @login.setter
    def login(self, new_login):
        """Set a new user login."""
        self.__login = new_login

    @password.setter
    def password(self, new_password):
        """Set a new user password."""
        self.__password = new_password

    @unit_name.deleter
    def unit_name(self):
        """Delete existing unit name."""
        del self.__unit_name

    @mac_address.deleter
    def mac_address(self):
        """Delete existing mac address."""
        del self.__mac_address

    @ip_address.deleter
    def ip_address(self):
        """Delete existing ip address."""
        del self.__ip_address

    @login.deleter
    def login(self):
        """Delete existing user login."""
        del self.__login

    @password.deleter
    def password(self):
        """Delete existing user password."""
        del self.__password
