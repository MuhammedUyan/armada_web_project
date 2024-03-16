from django.contrib import admin
from product.models import Product, ProductCategory, Slider

class CustomAdminSite(admin.AdminSite):
    site_header = 'Yeni Admin Panel Başlığı'

# Django varsayılan admin sitesini kaldırma
admin.site.site_header = 'Armada Site Yönetimi'

# Yeni özel admin sitesini kaydetme
custom_admin_site = CustomAdminSite(name='custom_admin')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'product_category',)
    search_fields = ('title',)
    readonly_fields = ('slug',)
    list_filter = ('product_category',)

    def product_category(self, obj):
        html = ""

        for product_category in obj.product_category.all():
            html += product_category.name + "<br>"
        return html


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    readonly_fields = ('slug',)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, CategoryAdmin)
admin.site.register(Slider)





