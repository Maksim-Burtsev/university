from django import forms

from main.models import Phone

class PhoneForm(forms.ModelForm):

    class Meta:
        model = Phone   
        fields = ['producer', 'model', 'photo_link', 'width', 'height', 'memory', 'price']

    