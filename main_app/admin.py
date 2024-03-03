from django.contrib import admin
from main_app.models import Post, Version, Product, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price_per_unit', 'category', 'is_published',)
    list_filter = ('category', 'is_published',)
    search_fields = ('name', 'description',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'content',)


@admin.register(Version)
class ProductVersionAdmin(admin.ModelAdmin):
    list_display = ('version_name', 'version_number', 'current_version')
