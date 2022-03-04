from django.shortcuts import render

from main.forms import TriangleForm
from main.models import Triangle

import math


def index(request):

    if request.method == "POST":
        form = TriangleForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)

            p = (obj.first_side+obj.second_side+obj.third_side)/2
            s = math.sqrt(p*(p-obj.first_side) *
                          (p-obj.second_side)*(p-obj.third_side))

            obj.area = round(s, 2)
            obj.save()
            
            area = round(s, 2)

    else:
        form = TriangleForm
        area = False

    context = {
        'form': form,
        'area' : area,
    }

    return render(request, 'main/index.html', context=context)
