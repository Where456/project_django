# main_app/urls.py
from django.urls import path
from .views import contacts, ProductDetailView, ProductsListView

app_name = 'main_app'

urlpatterns = [
    path('', ProductsListView.as_view(), name='product-list'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
