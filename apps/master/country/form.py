
from django import forms
from .models import Country
class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name', 'shortName', 'code', 'currency', 'order', 'disable']  
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter country name'}),
            'shortName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter short name'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter country code'}),
            'currency': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter currency'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter order'}),
            'disable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
        labels = {
            'name': 'Country Name',
            'shortName': 'Short Name',
            'code': 'Country Code',
            'currency': 'Currency',
            'order': 'Display Order',
            'disable': 'Disable Country',
        }
