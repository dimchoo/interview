from django.urls import path
from products.views import ProductListView, ProductDetailView, CategoriesListView, CategoryProductsDetailView


urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('categories/', CategoriesListView.as_view(), name='categories'),
    path('category/<int:pk>/', CategoryProductsDetailView.as_view(), name='category-detail')
]
