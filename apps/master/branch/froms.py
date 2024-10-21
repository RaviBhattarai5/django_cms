from django import forms
from .models import MasterBranch

class MasterBranchForm(forms.ModelForm):
    class Meta:
        model = MasterBranch
        fields = ['title', 'email', 'disable', 'code', 'brAddress', 'state', 'brType', 'isDealer', 'contactNo', 'isOTPValidation']
        
        # Customizing the appearance of form fields with widgets
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter branch title'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address'}),
            'disable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter branch code'}),
            'brAddress': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter branch address'}),
            'state': forms.Select(attrs={'class': 'form-control'}),  # Dropdown for selecting state
            'brType': forms.Select(attrs={'class': 'form-control'}),  # Dropdown for branch type (HO or BR)
            'isDealer': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'contactNo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact number'}),
            'isOTPValidation': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
        # Optional: Defining custom labels
        labels = {
            'title': 'Branch Title',
            'email': 'Email Address',
            'disable': 'Disable Branch',
            'code': 'Branch Code',
            'brAddress': 'Branch Address',
            'state': 'State',
            'brType': 'Branch Type',
            'isDealer': 'Is Dealer',
            'contactNo': 'Contact Number',
            'isOTPValidation': 'OTP Validation Required',
        }
