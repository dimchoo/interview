from django.views.generic import ListView
from products.models import Product


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()
    template_name = 'index.html'
