from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class ProductCategory(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Ürün Kategori"
        verbose_name_plural = "Ürün Kategorileri"


class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products')
    description = RichTextField()
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Ürün"
        verbose_name_plural = "Ürünler"

class Slider(models.Model):
    image = models.ImageField(upload_to='sliders')

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = "Vitrin"
        verbose_name_plural = "Vitrinler"