from django import forms
from .models import Transporter
from apps.master.tpl_ecc_charge.models import EccTransaction
from apps.master.area.models import Area  # Import Area for Select widget if needed

class TransporterForm(forms.ModelForm):
    class Meta:
        model = Transporter
        fields = ['area', 'transporter_name', 'gst_no', 'mobile_no1', 'mobile_no2', 
                  'tracking_url', 'min_weight_charge', 'min_weight', 'min_charge', 
                  'tpt_charge']

        widgets = {
            'area': forms.Select(attrs={
                'class': 'form-control', 
                'placeholder': 'Select Area'
            }),
            'transporter_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Transporter Name'
            }),
            'gst_no': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'GST Number'
            }),
            'mobile_no1': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Mobile No. 1'
            }),
            'mobile_no2': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Mobile No. 2 (Optional)'
            }),
            'tracking_url': forms.URLInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Tracking URL'
            }),
            'min_weight_charge': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Minimum Weight Charge'
            }),
            'min_weight': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Minimum Weight'
            }),
            'min_charge': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Minimum Charge'
            }),
            'tpt_charge': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Transport Charge'
            }),
        }


class EccTransactionForm(forms.ModelForm):
    class Meta:
        model = EccTransaction
        fields = ['transporter','ecc', 'amount']

        widgets = {
            'transporter': forms.Select(attrs={'class': 'form-control'}),

            'ecc': forms.Select(attrs={
                'class': 'form-control', 
                'placeholder': 'Select ECC'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Amount'
            }),
        }
