"""
2. Инкапсулировать оба параметра (название и цену) товара родительского класса.
Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.
Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
Результат выполнения заданий 1 и 2 должен быть идентичным.
"""


class ItemDiscount:
    _name = 'iPhone'
    _price = 100500


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'{super()._name} {super()._price}'


if __name__ == '__main__':
    parent = ItemDiscount()
    child = ItemDiscountReport()
    print(child.get_parent_data())


