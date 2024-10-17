from django import forms
from .models import FmsStage

class FmsStageForm(forms.ModelForm):
    class Meta:
        model = FmsStage
        fields = [
            'fms_stage_name', 'tat_mode', 'tat_value',
            'serial_no', 'is_active', 'created_by', 'updated_by',
            'deleted_by'
        ]
        widgets = {
            'fms_stage_name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 50}),
            'tat_mode': forms.Select(attrs={'class': 'form-control'}),
            'tat_value': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'serial_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'created_by': forms.Select(attrs={'class': 'form-control'}),
            'updated_by': forms.Select(attrs={'class': 'form-control'}),
            'deleted_by': forms.Select(attrs={'class': 'form-control'}),
        }
