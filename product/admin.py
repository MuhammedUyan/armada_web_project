from django.contrib import admin
from product.models import Product, ProductCategory, Slider


class CustomAdminSite(admin.AdminSite):
    site_header = 'Yeni Admin Panel Başlığı'

# Django varsayılan admin sitesini kaldırma
admin.site.site_header = 'Armada Site Yönetimi'

# Yeni özel admin sitesini kaydetme
custom_admin_site = CustomAdminSite(name='custom_admin')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category',)
    search_fields = ('title',)
    readonly_fields = ('slug',)
    list_filter = ('category',)

    def category(self, obj):
        html = ""

        for category in obj.categories.all():
            html += category.name + "<br>"
        return html

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    readonly_fields = ('slug',)


admin.site.register(Slider)
admin.site.register(Product)
admin.site.register(ProductCategory)





