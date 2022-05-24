from django.db import models


class Supplier(models.Model):
    name = models.CharField('Название', unique=True, max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Product(models.Model):
    name = models.CharField('Название', unique=True, max_length=64)
    receipt_date = models.DateTimeField('Дата поступления', null=True, blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, default=0)
    unit = models.CharField('Единица измерения', max_length=16, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, verbose_name='поставщик', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
