from django.shortcuts import render

from blog.models import Blog
from product.models import Product, ProductCategory, Slider


def index(request):
    context = {
        'sliders': Slider.objects.all(),
        "products": Product.objects.filter(is_home=True),
        'blogs': Blog.objects.filter(is_home= True),
    }
    return render(request, "product/index.html", context)


def product(request):
    context = {
        "products": Product.objects.all(),
        "categories": ProductCategory.objects.all()
    }
    return render(request, 'product/products.html', context)


def products_by_category(request, slug):
    context = {
        "products": Product.objects.filter(product_category__slug=slug),
        "categories": ProductCategory.objects.all(),
        "selected_category": slug
    }
    return render(request, "product/products.html", context)


