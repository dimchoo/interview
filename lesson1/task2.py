"""
2. Реализовать функцию print_directory_contents(path).
Функция принимает имя директории и выводит ее содержимое,
включая содержимое всех поддиректории (рекурсивно вызывая саму себя).
Использовать os.walk нельзя, но можно использовать os.listdir и os.path.isfile
"""
import os


some_path = os.path.abspath(os.path.dirname(__file__))


def print_directory_contents(path):
    for p in os.listdir(path):
        print(p)
        x = os.path.join(path, p)
        if os.path.isdir(x):
            print_directory_contents(x)


print_directory_contents(some_path)
