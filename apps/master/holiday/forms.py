from django import forms
from .models import Holidays  

class HolidaysForm(forms.ModelForm):
    class Meta:
        model = Holidays
        fields = ['sessionYr', 'holiday_Name', 'holiday_date', 'from_date', 'to_date', 'holidayType', 'is_active'] 
        widgets = {
            'holiday_date': forms.DateInput(attrs={'type': 'date'}), 
            'from_date': forms.DateInput(attrs={'type': 'date'}),
            'to_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'sessionYr': 'Session Year',
            'holiday_Name': 'Holiday Name',
            'holiday_date': 'Holiday Date',
            'from_date': 'From Date',
            'to_date': 'To Date',
            'holidayType': 'Holiday Type',
            'is_active': 'Is Active',
        }

    def clean(self):
        cleaned_data = super().clean()
        from_date = cleaned_data.get("from_date")
        to_date = cleaned_data.get("to_date")

       
        if from_date and to_date and from_date > to_date:
            raise forms.ValidationError("From Date cannot be later than To Date.")
