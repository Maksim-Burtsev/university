from django.shortcuts import render


def index(request):

    if request.method == 'POST':
        request.session['city'] = request.POST.get('city')
        request.session['age'] = request.POST.get('age')
        session = True

    if request.session.get('city'):
        context = {
            'city': request.session['city'],
            'age': request.session['age'],
            'session': True,
        }

    else:
        context = {
            'session': False,
        }

    return render(request, 'main/index.html', context=context)


def test(request):

    context = {
        'city': '',
        'age': '',
    }

    if request.session.get('city'):
        context['city'] = request.session.get('city')
        context['age'] = request.session.get('age')

    return render(request, 'main/test.html', context=context)
