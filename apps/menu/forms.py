from django import forms
from django.core.exceptions import ValidationError
from .models import Menu

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'title'}),
            'url': forms.TextInput(attrs={'class': 'form-control', 'id': 'url','required': False}),
            'icon': forms.TextInput(attrs={'class': 'form-control', 'id': 'icon','required': False}),
            'position': forms.NumberInput(attrs={'class': 'form-control', 'id': 'position'}),
            'publish' : forms.CheckboxInput(attrs={'class':'form-check-input', 'id': 'publish'}) 
            }