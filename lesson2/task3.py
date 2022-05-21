"""
3. Реализовать возможность переустановки значения цены товара в родительском классе.
Проверить, распечатать информацию о товаре.
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
    def get_parent_data(self):
        return f'{super()._name} {super()._price}'


if __name__ == '__main__':
    parent = ItemDiscount()
    parent.set_new_data('Nokia', 15)
    print(parent.name)
    print(parent.price)
    child = ItemDiscountReport()
    print(child.get_parent_data())
