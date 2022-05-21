"""
4. Реализовать расчет цены товара со скидкой.
Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса
(метод __init__, в который должна передаваться переменная — скидка),
и перегрузку метода __str__ дочернего класса.
В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
(вторая и третья строка после объявления дочернего класса).
"""


class ItemDiscount:
    _name = 'iPhone'
    _price = 100500

    def set_new_data(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, discount):
        self._discount = discount

    def __str__(self):
        new_price = super()._price - (super()._price / 100 * self._discount)
        return f'{super()._name} {new_price}'

    def get_parent_data(self):
        return f'{super()._name} {super()._price}'


if __name__ == '__main__':
    parent = ItemDiscount()
    print(ItemDiscountReport(5))
