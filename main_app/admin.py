from django.contrib import admin
from main_app.models import Post, Version, Product, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price_per_unit']
    # list_filter = ['category', 'is_published']
    search_fields = ['name', 'category']
    # list_editable = ['is_published']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'content',)


@admin.register(Version)
class ProductVersionAdmin(admin.ModelAdmin):
    list_display = ('version_name', 'version_number', 'current_version')
