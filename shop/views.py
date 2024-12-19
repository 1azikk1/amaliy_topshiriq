from django.shortcuts import render
from .models import Category, Product


def home(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'title': "Olma Shop"
    }
    return render(request, 'index.html', context)


def products_by_category(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    categories = Category.objects.get(pk=category_id)
    context = {
        'products': products,
        'title': f"{categories.name}: barcha mahsulotlar!"
    }
    return render(request, 'index.html', context)


def products_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product,
        'title': f"{product.name} haqida ma'lumotlar!"
    }
    return render(request, 'detail.html', context)

