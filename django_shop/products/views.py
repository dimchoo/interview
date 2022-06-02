from django.views.generic import ListView, DetailView
from products.models import Product, Category


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.select_related('supplier').prefetch_related('categories').all()
    template_name = 'index.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'


class CategoriesListView(ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = 'categories.html'


class CategoryProductsDetailView(DetailView):
    model = Category
    template_name = 'category-products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_products'] = Product.objects.filter(categories=self.object.pk)
        return context

