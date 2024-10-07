from django import forms
from .models import ProductBin

class ProductBinForm(forms.ModelForm):
    class Meta:
        model = ProductBin
        fields = ['title', 'disable', 'serialNo']  

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'disable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  
            'serialNo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter serial number'}),
        }

        labels = {
            'title': 'Title',
            'disable': 'Disable',
            'SerialNo': 'Serial Number',
        }
