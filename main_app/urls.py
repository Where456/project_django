from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from .views import ProductDetailView, contacts, ProductsListView, ProductDeleteView, ProductUpdateView, \
    ProductCreateView, PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView, VersionDetailView, \
    VersionCreateView, VersionUpdateView, restricted_access

urlpatterns = [
    path('', ProductsListView.as_view(), name='product-list'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product-detail'),
    path('product/form/', never_cache(ProductCreateView.as_view()), name='product-form'),
    path('product/delete/<int:pk>/', never_cache(ProductDeleteView.as_view()), name='product-delete'),
    path('product/edit/<int:pk>/', never_cache(ProductUpdateView.as_view()), name='product-edit'),

    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/form/', never_cache(PostCreateView.as_view()), name='post-form'),
    path('post/delete/<int:pk>/', never_cache(PostDeleteView.as_view()), name='post-delete'),
    path('post/edit/<int:pk>/', never_cache(PostUpdateView.as_view()), name='post-edit'),

    path('version/<int:version_id>/', VersionDetailView.as_view(), name='version-detail'),
    path('version/form/<int:pk>/', never_cache(VersionCreateView.as_view()), name='version-form'),
    path('version/edit/<int:pk>/', never_cache(VersionUpdateView.as_view()), name='version-edit'),
    path('restricted-access/', restricted_access, name='restricted-access'),

]