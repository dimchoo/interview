"""
5. Расширить программу из п. 4:
Усовершенствовать первую функцию из предыдущего примера.
Необходимо во втором списке часть строковых значений (выбирается случайно)
заменить на значения типа 345example (в обратном порядке, число и строка).
(То есть вы переделываете функцию записи в файл так, чтобы она иногда меняла запись на 345example)

Реализовать функцию поиска определенных подстрок в файле по следующим условиям:
вывод первого вхождения, вывод всех вхождений.

Реализовать функцию замену всех найденных подстрок на новое значение и вывод измененных строк.
(это ДВЕ ОТДЕЛЬНЫЕ функции которые ВЫВОДЯТ значения, не записывают и не модифицируют файлы)
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
            lists = [lst1, lst2]
            random_list1 = lists.pop(random.choice([0, -1]))
            random_list2 = lists[0]
            random_list1.append(f'{random.choice(string.ascii_letters)}')
            random_list2.append(random.randint(1, max_int))

        for k, v in dict(zip(lst1, lst2)).items():
            f.write(f'{k}{v}\n')

    return os.path.abspath(f_path)


def search(f_path, some_str):
    with open(f_path) as f:
        includes = []
        for line in f.readlines():
            if some_str in line:
                includes.append(line)
        if includes:
            print(f'Первое вхождение: {includes[0]}Все вхождения: {includes}')


def replace_includes(f_path, searched, replace_to):
    with open(f_path) as f:
        includes = []
        for line in f.readlines():
            if searched in line:
                includes.append(line)

        for s in includes:
            print(f'Было: {s}Стало: {s.replace(searched, replace_to)}')


if __name__ == '__main__':
    some_file = func1('test1', 10, 10)
    print('---SEARCH---')
    search(some_file, '1')
    print('------------')
    print('---REPLACE---')
    replace_includes(some_file, '1', '!!!')
    print('-------------')
