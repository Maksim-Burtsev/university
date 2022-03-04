from django.shortcuts import render

from main.models import Product

import random


def index(request):

    flag = True

    if request.method == 'POST':
        products = Product.objects.order_by('-price')[:5]
        flag = False

    else:
        products = Product.objects.all()

    context = {
        'products': products,
        'flag': flag,
    }

    return render(request, 'main/index.html', context=context)
