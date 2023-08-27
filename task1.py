# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
from functools import wraps
import json
from random import randint
from typing import Callable


def launch(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with open('csv_file.csv', 'r', newline='') as f:
            data = csv.reader(f)
            for i in data:
                line = ''.join(i).split(' ')
                result = func(line)
                print(result)
        return result
    return wrapper


def our_cash(func: Callable):
    try:
        with open(f'{func.__name__}.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

        def wrapper(*args):
            arg = str(args)
            result = func(*args)
            data.update({arg: result})

            with open(f'{func.__name__}.json', 'w') as f:
                json.dump(data, f, indent=4)

            return result
        return wrapper


def csv_create_file():
    nums = 3
    with open('csv_file.csv', 'w', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(
            f, dialect='excel', delimiter=' ', quoting=csv.QUOTE_MINIMAL)
        for _ in range(randint(100, 1001)):
            line = []
            for _ in range(nums):
                line.append(randint(1, 100))
            csv_write.writerow(line)


@launch
@our_cash
def equation_solving(nums_list: list):
    # a, b, c = nums_list[0], nums_list[1], nums_list[2]
    a = int(nums_list[0])
    b = int(nums_list[1])
    c = int(nums_list[2])
    result = b**2 - 4*a*c
    if result < 0:
        return 'No result'
    elif result == 0:
        return (-b / (2*a))
    else:
        x1 = (-b + (result)**0.5)/(2*a)
        x2 = (-b - (result)**0.5) / (2*a)
        return (x1, x2)


if __name__ == '__main__':
    csv_create_file()
    equation_solving()
