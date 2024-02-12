from django.urls import path
from .views import ProductDetailView, contacts, ProductsListView, ProductDeleteView, ProductUpdateView, \
    ProductCreateView, PostListView, PostDetailView, PostCreateView, PostDeleteView, PostUpdateView, VersionDetailView, \
    VersionCreateView, VersionUpdateView, restricted_access

urlpatterns = [
    path('', ProductsListView.as_view(), name='product-list'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/form/', ProductCreateView.as_view(), name='product-form'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
    path('product/edit/<int:pk>/', ProductUpdateView.as_view(), name='product-edit'),

    path('posts/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/form/', PostCreateView.as_view(), name='post-form'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/edit/<int:pk>/', PostUpdateView.as_view(), name='post-edit'),

    path('version/<int:version_id>/', VersionDetailView.as_view(), name='version-detail'),
    path('version/form/<int:pk>/', VersionCreateView.as_view(), name='version-form'),
    path('version/edit/<int:pk>/', VersionUpdateView.as_view(), name='version-edit'),
    path('restricted-access/', restricted_access, name='restricted-access'),

]