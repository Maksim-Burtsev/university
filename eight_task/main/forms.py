from django import forms

from main.models import Player


class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        fields = ('name', 'number', 'team', 'photo', 'wiki_link')

