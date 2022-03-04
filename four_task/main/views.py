from audioop import reverse
from django.shortcuts import render, redirect

from main.models import Phone
from main.forms import PhoneForm


def index(request):

    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    if request.GET.get('query'):
        search = request.GET.get('query')
        phones = Phone.objects.filter(model__icontains=search)

    else:
        phones = Phone.objects.all()
        
    form = PhoneForm()
    context = {
        'phones' : phones,
        'form' : form,
    }

    return render(request, 'main/index.html', context=context)

def edit(request, post_pk):

    if request.method == "POST":
        phone = Phone.objects.get(pk=post_pk)
        form = PhoneForm(request.POST, instance=phone)
        if form.is_valid():
            form.save()
            return redirect('edit', post_pk=post_pk)

    phone = Phone.objects.get(pk=post_pk)
    form = PhoneForm(instance=phone)

    context = {
        'form' : form,
        'phone' : phone,
    }

    return render(request, 'main/edit.html', context=context)