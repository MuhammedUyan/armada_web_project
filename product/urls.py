from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("index/", views.index),
    path("product_category/<slug:slug>", views.products_by_category, name="products_by_category"),
    path('products/', views.product, name='products')
]
