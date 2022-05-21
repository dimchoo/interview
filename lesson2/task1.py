"""
1. Создать два класса. Первый — родительский (ItemDiscount),
должен содержать статическую информацию о товаре: название и цену.
Второй — дочерний (ItemDiscountReport),
должен содержать функцию (get_parent_data),
отвечающую за отображение информации о товаре в одной строке
вида (“{название товара} {цена товара}”).
Создать экземпляры родительского класса и дочернего. Распечатать информацию о товаре.
"""


class ItemDiscount:
    name = 'iPhone'
    price = 100500


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        return f'{super().name} {super().price}'


if __name__ == '__main__':
    parent = ItemDiscount()
    child = ItemDiscountReport()
    print(child.get_parent_data())
