from django.urls import path
from . import views
# http://localhost:8000/          => homepage
# http://localhost:8000/index     => homepage
# http://localhost:8000/blogs     => blogs
# http://localhost:8000/blogs/3   => blogs-details


urlpatterns = [
    path("", views.index, name="home"),
    path("index/", views.index),
    path("blogs/", views.blogs, name="blogs"),
    path("category/<slug:slug>", views.blogs_by_category, name="blogs_by_category"),
    path("blogs/<slug:slug>", views.blog_details, name="blog_details"),
]