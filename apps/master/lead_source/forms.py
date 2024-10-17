from django import forms
from .models import LeadSource

class LeadSourceForm(forms.ModelForm):
    class Meta:
        model = LeadSource
        fields = [
            'lead_source_code', 'lead_source_name', 'is_lead_generate_by', 
            'is_lead_assign_to', 'is_re_generate_by', 'is_re_assign_to', 
            'is_lead_created_by', 'is_active', 'created_by', 'updated_by', 'user'
        ]
        widgets = {
            'lead_source_code': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 30}),
            'lead_source_name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 100}),
            'is_lead_generate_by': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_lead_assign_to': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_re_generate_by': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_re_assign_to': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_lead_created_by': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'created_by': forms.Select(attrs={'class': 'form-control'}),
            'updated_by': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }
