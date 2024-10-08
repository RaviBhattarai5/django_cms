from django import forms
from .models import State

class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['country', 'stateCode', 'stateName', 'capitalName', 'disable']  
        
        widgets = {
            'country': forms.Select(attrs={'class': 'form-control'}),  
            'stateCode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter state code'}),
            'stateName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter state name'}),
            'capitalName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter capital name'}),
            'disable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
      
        labels = {
            'country': 'Country',
            'stateCode': 'State Code',
            'stateName': 'State Name',
            'capitalName': 'Capital Name',
            'disable': 'Disable State',
        }