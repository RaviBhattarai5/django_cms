from django import forms
from .models import MasterGroup
from django.contrib.auth.models import User


class MasterGroupForm(forms.ModelForm):
    class Meta:
        model = MasterGroup
        fields = ['group_name', 'category_id', 'is_active', 'created_by','created_date',
            'updated_by','updated_date','deleted_by', 'deleted_date',
        ]
        widgets = {
            'group_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Group Name'}),
            'category_id': forms.Select(attrs={'class': 'form-select'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'created_by': forms.Select(attrs={'class': 'form-select'}),  
            'created_date': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD HH:MM:SS' }),
            'updated_by': forms.Select(attrs={'class': 'form-select'}),
            'updated_date': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD HH:MM:SS' }),
            'deleted_by': forms.Select(attrs={'class': 'form-select'}),
            'deleted_date': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD HH:MM:SS'}),
        }

