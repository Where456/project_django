from django.contrib import admin

from main_app.models import Category, Product, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_unit', 'category',)
    list_filter = ('name', 'description', 'category',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'creation_date', 'is_published', 'views_count')
    list_filter = ('creation_date', 'is_published')
    search_fields = ('title', 'content')

