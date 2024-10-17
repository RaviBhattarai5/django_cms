from django import forms
from .models import ECCMaster

class ECCMasterForm(forms.ModelForm):
    class Meta:
        model = ECCMaster
        fields = ['weight_from', 'weight_to', 'serial_no', 'is_active']
        widgets = {
            'weight_from': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'weight_to': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'serial_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
