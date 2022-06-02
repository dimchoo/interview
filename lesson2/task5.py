"""
5. Проверить на практике возможности полиморфизма.
Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно.
Внутри каждого поместить функцию get_info,
которая в первом классе будет отвечать за вывод названия товара, а вторая — его цены.
Далее реализовать вызов каждой из функции get_info.
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


class ItemDiscountReportName(ItemDiscount):
    def get_info(self):
        return f'{super()._name}'


class ItemDiscountReportPrice(ItemDiscount):
    def get_info(self):
        return f'{super()._price}'


if __name__ == '__main__':
    c1 = ItemDiscountReportName()
    c2 = ItemDiscountReportPrice()
    print(c1.get_info())
    print(c2.get_info())
