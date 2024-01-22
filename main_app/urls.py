from django.urls import path
from .views import product_list_view, ProductDetailView, contacts

urlpatterns = [
    path('', product_list_view, name='product_list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/', contacts, name='contacts'),
]
