"""
Усовершенствовать программу «Банковский депозит».
Третьим аргументом в функцию должна передаваться фиксированная ежемесячная сумма пополнения вклада.
Считаем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего.
Если 3м аргументом передан 0, то вызов должен быть совпадать с задачей 4.
"""
from lesson1.task4 import bank


def refill_depo(depo_sum, period, refill):
    d = depo_sum
    for i in range(period-2):
        d += refill
    return d


def bank_upgrade(depo_sum, period, refill=0):
    if refill:
        _depo = refill_depo(depo_sum, period, refill)
        print(_depo)
        return bank(_depo, period)
    return bank(depo_sum, period)


print(bank_upgrade(1000, 6, 100))
