from django.urls import path
from .views import home, products_by_category, products_detail

urlpatterns = [
    path('', home, name='home'),
    path('categories/<int:category_id>/', products_by_category, name='products_by_category'),
    path('product/<int:product_id>/', products_detail, name='product_detail'),
]

