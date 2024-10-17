
from django import forms
from .models import HolidaysType

class HolidaysTypeForm(forms.ModelForm):
    class Meta:
        model = HolidaysType
        fields = ['name', 'short_name', 'is_active', 'holidays_type']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'short_name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'holidays_type': forms.TextInput(attrs={'class': 'form-control'}),
        }
