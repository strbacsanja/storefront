from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product, OrderItem

# Create your views here.

def say_hello(request):
    queryset = Product.objects.only('id', 'title')



    return render(request, 'hello.html', {'name': 'Sanja', 'products': list(queryset)})