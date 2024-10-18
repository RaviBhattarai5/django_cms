from django import forms
from .models import FmsContact

class FmsContactForm(forms.ModelForm):
    class Meta:
        model = FmsContact
        fields = [
            'area', 'fms_stage', 'contact_name', 'contact_no',
            'email_id', 'is_active', 'created_by', 'updated_by', 'deleted_by'
        ]
        widgets = {
            'area': forms.Select(attrs={'class': 'form-control'}),
            'fms_stage': forms.Select(attrs={'class': 'form-control'}),
            'contact_name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 200}),
            'contact_no': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 10}),
            'email_id': forms.EmailInput(attrs={'class': 'form-control', 'maxlength': 200}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'created_by': forms.Select(attrs={'class': 'form-control'}),
            'updated_by': forms.Select(attrs={'class': 'form-control'}),
            'deleted_by': forms.Select(attrs={'class': 'form-control'}),
        }
