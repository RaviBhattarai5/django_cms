from django import forms
from .models import FmsStatus

class FmsStatusForm(forms.ModelForm):
    class Meta:
        model = FmsStatus
        fields = [
            'fms_action_type','fms_status_code','fms_status_name','parent_id','serial_no','is_active','created_by','updated_by','deleted_by','deleted_date',
        ]
        widgets = {
            'fms_action_type': forms.TextInput(attrs={'class': 'form-control'}),
            'fms_status_code': forms.TextInput(attrs={'class': 'form-control'}),
            'fms_status_name': forms.TextInput(attrs={'class': 'form-control'}),
            'parent_id': forms.Select(attrs={'class': 'form-control'}),
            'serial_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'created_by': forms.Select(attrs={'class': 'form-control'}),
            'updated_by': forms.Select(attrs={'class': 'form-control'}),
            'deleted_by': forms.Select(attrs={'class': 'form-control'}),
            'deleted_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
