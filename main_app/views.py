from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main_app.models import Product


def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(f'{name}: {email}')
    return render(request, 'contacts.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main_app/product_detail.html'
    context_object_name = 'product'
