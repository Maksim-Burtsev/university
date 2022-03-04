from django import forms

from main.models import Triangle

class TriangleForm(forms.ModelForm):

    class Meta:
        model=Triangle
        fields = ('first_side', 'second_side', 'third_side')