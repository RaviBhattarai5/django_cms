from django import forms
from .models import CustomerMaster  

class CustomerMasterForm(forms.ModelForm):
    class Meta:
        model = CustomerMaster
        fields = ['contact_name', 'company_name', 'address', 'mobile', 'email'] 

        widgets = {
            'contact_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ''}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),  
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),  
        }
