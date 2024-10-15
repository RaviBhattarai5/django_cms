from django import forms
from .models import PickList

class PickListForm(forms.ModelForm):
    class Meta:
        model = PickList
        fields = ['pick_list_name', 'parent', 'is_active', 'serial_no']

        widgets = {
            'pick_list_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pick List Name'}),
            'parent': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'serial_no': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Serial Number'}),
        }
