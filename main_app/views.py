from django.shortcuts import render

from main_app.models import Product


def home(request):
    data = Product.objects.all()
    return render(request, 'home.html', {'data': data})


def contact(request):
    return render(request, 'contact.html')
