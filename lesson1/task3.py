"""
3. Разработать целочисленный генератор случайных чисел.
В функцию передавать начальную и конечную границу диапазона генерации
(выдавать значения из диапазона включая концы).
Заполнить этими данными словарь.
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”,
а значене сгенеренное случайное число.  Вывести содержимое словаря.
(Усложненный вариант по желанию*): Не использовать стандартный модуль python random.
"""

import time
import struct


def last_bit(f):
    return struct.pack('!f', f)[-1] & 1


def get_rand_bits(k):
    result = 0
    for _ in range(k):
        time.sleep(0)
        result <<= 1
        result |= last_bit(time.process_time())
    return result


def randbelow(n):
    if n <= 0:
       raise ValueError
    k = n.bit_length()
    r = get_rand_bits(k)
    while r >= n:
        r = get_rand_bits(k)
    return r


def my_randint(a, b):
    return a + randbelow(b - a + 1)


def res_func(start, stop):
    return {f'elem_{i}': my_randint(start, stop) for i in range(start, stop+1)}


print(res_func(2, 8))


