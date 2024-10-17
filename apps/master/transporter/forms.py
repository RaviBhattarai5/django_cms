from django import forms
from .models import Transporter

class TransporterForm(forms.ModelForm):
    class Meta:
        model = Transporter
        fields = [
            'area', 'transporter_name', 'gst_no', 'mobile_no1', 'mobile_no2', 
            'tracking_url', 'is_active', 'min_weight_charge', 'min_weight', 
            'min_charge', 'tpt_charge'
        ]
        widgets = {
            'area': forms.Select(attrs={'class': 'form-control'}),
            'transporter_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Transporter Name'}),
            'gst_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'GST No'}),
            'mobile_no1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile No 1'}),
            'mobile_no2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile No 2'}),
            'tracking_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Tracking URL'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'min_weight_charge': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'min_weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'min_charge': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'tpt_charge': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
