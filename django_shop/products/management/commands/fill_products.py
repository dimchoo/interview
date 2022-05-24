from django.core.management.base import BaseCommand
import random
from products.models import Supplier, Product


SUPPLIER_TEST_DATA = [
    {'name': 'Coca-Cola Co'},
    {'name': 'Procter & Gamble'},
    {'name': 'Apple'},
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
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        Supplier.objects.all().delete()
        Product.objects.all().delete()

        Supplier.objects.bulk_create([Supplier(**i) for i in SUPPLIER_TEST_DATA])
        ids = list(Supplier.objects.all().values_list('id', flat=True))
        print('Suppliers done!')

        Product.objects.bulk_create([Product(**i, supplier_id=random.choice(ids)) for i in PRODUCT_TEST_DATA])
        print('Products done!')
