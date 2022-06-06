from django.contrib import admin
from products.models import Supplier, Product, Category


admin.site.register(Supplier)
admin.site.register(Category)
admin.site.register(Product)
