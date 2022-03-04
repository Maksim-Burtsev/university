from django.shortcuts import render

from main.models import Numbers, Category


def index(request):

    cats = Category.objects.all().prefetch_related('nums')

    context = {
        'cats' : cats,
    }

    return render(request, 'main/index.html', context=context)
