from django import forms
from .models import City

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'state','disable']  
        
        widgets = {
            'state': forms.Select(attrs={'class': 'form-control'}),  
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter City name'}),
            'disable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'state': 'State',
            'name': 'Name',
            'disable': 'Disable City',
        }