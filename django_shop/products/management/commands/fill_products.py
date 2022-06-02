from django.core.management.base import BaseCommand
import random
from products.models import Supplier, Category, Product


SUPPLIER_TEST_DATA = [
    {'name': 'Coca-Cola Co'},
    {'name': 'Procter & Gamble'},
    {'name': 'Apple'},
]

CATEGORIES_TEST_DATA = [
    {'name': 'Напитки'},
    {'name': 'Техника'},
    {'name': 'Кондитерские изделия'},
]


PRODUCT_TEST_DATA = [
    {
        'name': 'Fanta',
        'price': round(random.random() * 10000, 2),
    },
    {
        'name': 'iPhone',
        'price': round(random.random() * 10000, 2),
    },
    {
        'name': 'Картошка',
        'price': round(random.random() * 10000, 2),
    },
    {
        'name': 'Сок',
        'price': round(random.random() * 10000, 2),
    },
    {
        'name': 'Курица',
        'price': round(random.random() * 10000, 2),
    },
    {
        'name': 'Халва',
        'price': round(random.random() * 10000, 2),
    },
    {
        'name': 'Coca-Cola',
        'price': round(random.random() * 10000, 2),
    },
    {
        'name': 'Kinder',
        'price': round(random.random() * 10000, 2),
    },

]


class Command(BaseCommand):
    def handle(self, *args, **options):
        Supplier.objects.all().delete()
        Category.objects.all().delete()
        Product.objects.all().delete()

        Supplier.objects.bulk_create([Supplier(**i) for i in SUPPLIER_TEST_DATA])
        sup_ids = list(Supplier.objects.all().values_list('id', flat=True))
        print('Suppliers done!')

        Category.objects.bulk_create([Category(**i) for i in CATEGORIES_TEST_DATA])
        cat_ids = list(Supplier.objects.all().values_list('id', flat=True))
        print('Categories done!')

        Product.objects.bulk_create([Product(**i, supplier_id=random.choice(sup_ids)) for i in PRODUCT_TEST_DATA])
        for product in Product.objects.all().iterator():
            product.categories.set(list(set([random.choice(cat_ids), random.choice(cat_ids)])))
        print('Products done!')
