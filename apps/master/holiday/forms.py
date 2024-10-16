from django import forms
from .models import Holidays  

class HolidaysForm(forms.ModelForm):
    class Meta:
        model = Holidays
        fields = ['session_year', 'holiday_name', 'holiday_date', 'from_date', 'to_date', 'holiday_type', 'is_active'] 
        widgets = {
            'holiday_date': forms.DateInput(attrs={'type': 'date', 'class':'form-control'}), 
            'from_date': forms.DateInput(attrs={'type': 'date', 'class':'form-control'}),
            'to_date': forms.DateInput(attrs={'type': 'date', 'class':'form-control'}),
            'holiday_type':forms.Select(attrs={'class':'form-control'}),
            'holiday_name':forms.TextInput(attrs={'class':'form-control'}),
        }
        labels = {
            'sessionYr': 'Session Year',
            'holiday_Name': 'Holiday Name',
            'holiday_date': 'Holiday Date',
            'from_date': 'From Date',
            'to_date': 'To Date',
            'holiday_type': 'Holiday Type',
            'is_active': 'Is Active',
        }

        error_messages = {
            'holiday_name': {'required': 'Holiday name cannot be blank.'},
            'holiday_type': {'required': 'Holiday date is required.'},
        }

    def clean(self):
        cleaned_data = super().clean()
        from_date = cleaned_data.get("from_date")
        to_date = cleaned_data.get("to_date")

       
        if from_date and to_date and from_date > to_date:
            raise forms.ValidationError("From Date cannot be later than To Date.")
