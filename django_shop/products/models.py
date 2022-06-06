from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager


class Supplier(models.Model):
    name = models.CharField('Название', unique=True, max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Category(models.Model):
    name = models.CharField('Название', unique=True, max_length=64)
    site = models.ForeignKey(Site, on_delete=models.CASCADE, verbose_name='Сайт', related_name='categories', null=True)
    site_objects = CurrentSiteManager('site')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField('Название', unique=True, max_length=64)
    receipt_date = models.DateTimeField('Дата поступления', null=True, blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2, default=0)
    unit = models.CharField('Единица измерения', max_length=16, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, verbose_name='Поставщик', on_delete=models.CASCADE,
                                 null=True, blank=True,
                                 related_name='products')
    categories = models.ManyToManyField(Category, verbose_name='Категории',
                                        null=True, blank=True, related_name='products')

    site = models.ManyToManyField(Site, verbose_name='Сайт', related_name='products', null=True)
    site_objects = CurrentSiteManager('site')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
