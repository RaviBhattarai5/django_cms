from django import forms
from .models import TransporterArea

class TransporterAreaForm(forms.ModelForm):
    class Meta:
        model = TransporterArea
        fields = [
            'transporter',
            'city',
            'min_weight',
            'min_charge',
            'tpt_charge',
            'ecc_charge',
            'fuel_surcharge',
            'currency_adjustment_factor',
            'docket_fees',
            'rov',
            'mcc',
            'oda',
            'ss',
            'annual_hike',
            'is_active',
            'updated_by'
        ]
        widgets = {
            'transporter':forms.Select(attrs={'step': '0.01', 'class':'form-control'}),
            'city':forms.Select(attrs={'step': '0.01', 'class':'form-control'}),
            'min_weight': forms.NumberInput(attrs={'step': '0.01', 'class':'form-control'}),
            'min_charge': forms.NumberInput(attrs={'step': '0.01', 'class':'form-control'}),
            'tpt_charge': forms.NumberInput(attrs={'step': '0.01', 'class':'form-control'}),
            'ecc_charge': forms.NumberInput(attrs={'step': '0.01', 'class':'form-control'}),
            'fuel_surcharge': forms.NumberInput(attrs={'step': '0.01', 'class':'form-control'}),
            'currency_adjustment_factor': forms.NumberInput(attrs={'step': '0.01', 'class':'form-control'}),
            'docket_fees': forms.NumberInput(attrs={'step': '0.01', 'class':'form-control'}),
            'rov': forms.NumberInput(attrs={'step': '0.01', 'class':'form-control'}),
            'mcc': forms.NumberInput(attrs={'step': '0.01', 'class':'form-control'}),
            'oda': forms.NumberInput(attrs={'step': '0.01', 'class':'form-control'}),
            'ss': forms.NumberInput(attrs={'step': '0.01', 'class':'form-control'}),
            'annual_hike': forms.NumberInput(attrs={'step': '0.01', 'class':'form-control'}),
            'updated_by': forms.TextInput(attrs={'placeholder': 'User ID'}),
        }

    def __init__(self, *args, **kwargs):
        super(TransporterAreaForm, self).__init__(*args, **kwargs)
        # Optionally, you can set custom labels or help texts
        self.fields['transporter'].label = "Transporter"
        self.fields['city'].label = "City"
        self.fields['is_active'].label = "Is Active"
