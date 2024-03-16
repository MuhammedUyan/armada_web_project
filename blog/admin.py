from django.contrib import admin
from .models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_home', 'slug', 'category')
    list_editable = ('is_home',)
    search_fields = ('title', 'description')
    readonly_fields = ('slug',)
    list_filter = ('is_home', 'category')

    def category(self, obj):
        html = ""

        for category in obj.categories.all():
            html += category.name + "<br>"
        return html

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    readonly_fields = ('slug',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
