from django.shortcuts import render
from django.shortcuts import redirect


from main.models import Player, Team
from main.forms import PlayerForm

def index(request):

    flag = True
    if request.GET.get('query'):
        search = request.GET.get('query')

        teams = Team.objects.all()
        team_names = [team.name for team in teams]
        print(team_names)
        for name in team_names:
            if search.lower() in name.lower():
                players = Player.objects.filter(team__name=name)
                flag = False
                break
    if flag and request.GET.get('query'):
        search = request.GET.get('query')
        players = Player.objects.filter(name__icontains=search)

    if not request.GET.get('query'):
        players = Player.objects.all()

    context = {
        'players': players,
    }

    return render(request, 'main/index.html', context=context)

def add(request):

    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = PlayerForm()
    
    context = {
        'form' : form,
    }

    return render(request, 'main/add.html', context=context)
