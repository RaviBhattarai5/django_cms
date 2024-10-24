from django import forms
from .models import EnquiryStatus

class EnquiryStatusForm(forms.ModelForm):
    class Meta:
        model = EnquiryStatus
        fields = [
            'case_study',
            'enquiry_status_name',
            'enquiry_stage_id',
            'remarks',
            'is_active',
            'created_by',
            'updated_by',
        ]
        widgets = {
            'case_study': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter case study'}),
            'enquiry_status_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter enquiry status name'}),
            'enquiry_stage_id': forms.Select(attrs={'class': 'form-control'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter remarks', 'rows': 3}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            # 'CreatedBy': forms.Select(attrs={'class': 'form-control'}),
            # 'UpdatedBy': forms.Select(attrs={'class': 'form-control'}),
        }
