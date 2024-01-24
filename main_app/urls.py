from django.urls import path
from .views import ProductDetailView, contacts, ProductsListView, PostListView, PostDetailView, PostCreateView, \
    PostDeleteView, PostUpdateView

urlpatterns = [
    path('', ProductsListView.as_view(), name='product_list'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/form/', PostCreateView.as_view(), name='post-form'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='post-edit'),
]