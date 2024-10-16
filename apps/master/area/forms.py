from django import forms
from .models import Area

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['name', 'email','disable','has_go_down','sr_email','gst_no','address','area_code','state','city','pin_code']  
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Area name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'has_go_down': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sr_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'gst_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter GST Number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Address'}),
            'area_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Area Code'}),
            'state': forms.Select(attrs={'class': 'form-control'}),  
            'city': forms.Select(attrs={'class': 'form-control'}),
            'pin_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Pin Code'}),
            'disable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }