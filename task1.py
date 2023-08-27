# Напишите следующие функции: 
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
from random import randint

def csv_create_file():
    nums = 3 
    with open ('csv_file.csv', 'w', newline='', encoding='utf-8') as f:
        csv_write = csv.writer(f, dialect='excel', delimiter=' ', quoting=csv.QUOTE_MINIMAL)
        for _ in range (randint (100,1001)):
            line =[]
            for _ in range (nums):
                line.append(randint(1,100))
            csv_write.writerow(line)

if __name__ == '__main__':
    csv_create_file()