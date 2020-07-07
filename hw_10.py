import time
# Задача-1
# У вас есть файл из нескольких строк. Нужно создать генератор который будет построчно выводить строки из вашего файла.
# При вызове итерировании по генератору необходимо проверять строки на уникальность.
# Если строка уникальна, тогда ее выводим на экран, если нет - скипаем


def my_gen(file):
    """Generator for checking the unique strings in txt file, which become printed."""
    with open(file, 'r') as file_to_read:
        work_strings = file_to_read.read()
    for line in work_strings.splitlines():
        if len(line) > len(set(line)):
            yield line
            print(line)
        continue


string_gen = my_gen('hw_10.txt')
next(string_gen)
next(string_gen)
next(string_gen)
next(string_gen)
next(string_gen)
next(string_gen)


# Задача-2:
# представим есть файл с логами, его нужно бессконечно контролировать
# на предмет возникнования заданных сигнатур.
#
# Необходимо реализовать пайплайн из корутин, который подключается к существующему файлу
# по принципу команды tail, переключается в самый конец файла и с этого момента начинает следить
# за его наполнением, и в случае возникнования запиcей, сигнатуры которых мы отслеживаем -
# печатать результат

def coroutine(func):
    """Decorator to call next() method of the generator object function. """
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start


@coroutine
def grep(pattern, target):
    """This generator founds and sends a looking pattern in the file. """
    try:
        while True:
            line = yield
            if pattern in line:
                target.send(line)
    except StopIteration:
        print('I so tired..')


@coroutine
def printer():
    """This function only prints the getted pattern. """
    while True:
        line = yield
        print(line)


@coroutine
def dispenser(targets):
    """This function translates gotted data to another functions."""
    while True:
        item = yield
        for target in targets:
            target.send(item)


def follow(file, target):
    """This function connects to the file, goes the end and waiting for appearence a new log strings in the file. """
    file.seek(0, 2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        target.send(line)


f_open = open('log.txt')
follow(f_open,
       dispenser([
           grep('python', printer()),
           grep('is', printer()),
           grep('great', printer()),
       ])
       )
