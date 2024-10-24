from django import forms
from .models import EnquiryStage

class EnquiryStageForm(forms.ModelForm):
    class Meta:
        model = EnquiryStage
        fields = ['enquiry_stage_name', 'serial_no', 'is_active']  # Fields to include in the form

        # Optional: You can customize widgets if needed
        widgets = {
            'enquiry_stage_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Enquiry Stage Name'}),
            'serial_no': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Serial Number'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
