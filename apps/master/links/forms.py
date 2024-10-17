from django import forms
from .models import Link

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = [
            'link_type', 'link_title', 'link_value', 
            'start_date', 'end_date', 'is_active', 
            'created_by', 'updated_by', 'deleted_by'
        ]
        widgets = {
            'link_type': forms.Select(attrs={'class': 'form-control'}),
            'link_title': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 500}),
            'link_value': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 1000}),
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'created_by': forms.Select(attrs={'class': 'form-control'}),
            'updated_by': forms.Select(attrs={'class': 'form-control'}),
            'deleted_by': forms.Select(attrs={'class': 'form-control'}),
        }
