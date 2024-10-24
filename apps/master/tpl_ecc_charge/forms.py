from django import forms
from .models import EccTransaction

class EccTransactionForm(forms.ModelForm):
    class Meta:
        model = EccTransaction
        fields = [
            'transporter', 'ecc', 'amount', 'is_active'
        ]
        widgets = {
            'transporter': forms.Select(attrs={'class': 'form-control'}),
            'ecc': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
