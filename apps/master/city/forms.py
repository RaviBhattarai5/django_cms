from django import forms
from .models import State

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['country', 'state_code', 'state_name', 'capital_name', 'disable']  
        
        widgets = {
            'country': forms.Select(attrs={'class': 'form-control'}),  
            'state_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter state code'}),
            'state_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter state name'}),
            'capital_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter capital name'}),
            'disable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'country': 'Country',
            'state_code': 'State Code',
            'state_name': 'State Name',
            'capital_name': 'Capital Name',
            'disable': 'Disable State',
        }