"""
4. Написать программу «Банковский депозит».
Клиент банка делает депозит на определенный срок.

В зависимости от суммы и срока вклада определяется процентная ставка:
1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 и более года — 5 % годовых).
10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 и более года – 6.5 % годовых).
100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 и более года — 7.5 % годовых).

Проценты начисляются на депозит в конце каждого месяца.

Необходимо написать функцию,
в которую будут передаваться параметры:
сумма вклада и срок вклада (в месяцах), а на выходе возвращать сумму вклада на конец срока.
"""


def get_profit_depo(depo_sum, period, p6, p12, p24):
    if period >= 24:
        one_year = depo_sum / 100 * p24
        return one_year * 2 + depo_sum
    elif period >= 12:
        one_year = depo_sum / 100 * p12
        return one_year + depo_sum
    elif period >= 6:
        one_year = depo_sum / 100 * p6
        return one_year / 2 + depo_sum
    else:
        return depo_sum


def bank(depo_sum, period):
    if depo_sum > 100000:
        return get_profit_depo(depo_sum, period, 7, 8, 7.5)
    elif depo_sum > 10000:
        return get_profit_depo(depo_sum, period, 6, 7, 6.5)
    elif depo_sum >= 1000:
        return get_profit_depo(depo_sum, period, 5, 6, 5)
    else:
        return depo_sum


# print(bank(1000, 12))
