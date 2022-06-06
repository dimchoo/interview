"""
4. Написать программу, в которой реализовать две функции.
В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение и завершаем работу.
Необходимо открыть файл и создать два списка: с текстовой и числовой информацией.
Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение (например example345).
Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл.
Во второй функции необходимо реализовать открытие файла и простой, построчный вывод содержимого
"""
import os
import string
import random


def func1(f_path, string_count, max_int):
    if os.path.exists(f_path):
        print('Файл существует!')
        return

    with open(f_path, 'w', encoding='utf-8') as f:
        lst1 = []
        lst2 = []
        for _ in range(string_count):
            lst1.append(f'{random.choice(string.ascii_letters)}')
            lst2.append(random.randint(1, max_int))

        for k, v in dict(zip(lst1, lst2)).items():
            f.write(f'{k}{v}\n')

    return os.path.abspath(f_path)


def func2(f_path):
    if f_path:
        with open(f_path) as f:
            for line in f.readlines():
                print(line.replace('\n', ''))


if __name__ == '__main__':
    func2(func1('test.txt', 10, 10))
