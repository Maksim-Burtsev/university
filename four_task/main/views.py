from django.shortcuts import render

from main.models import Phone


def index(request):

    phones = Phone.objects.all()
    context = {
        'phones' : phones,
    }

    return render(request, 'main/index.html', context=context)
