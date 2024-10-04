from django import forms
from .models import PermissionType

class PermissionTypeForm(forms.ModelForm):
    class Meta:
        model = PermissionType
        fields = ['name', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
