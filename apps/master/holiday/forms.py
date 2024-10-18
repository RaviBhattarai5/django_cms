# forms.py
from django import forms
from .models import Holidays
from apps.master.area.models import Area

class HolidaysForm(forms.ModelForm):
    holiday_in_area = forms.ModelMultipleChoiceField(
        queryset=Area.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control js-example-basic-multiple'}),  
        required=False
    )

    class Meta:
        model = Holidays
        fields = [
            'session_year', 
            'holiday_name', 
            'holiday_date', 
            'from_date', 
            'to_date', 
            'holiday_type', 
            'holiday_in_area', 
            'is_active'
        ]
        widgets = {
            'holiday_type': forms.Select(attrs={'class': 'form-control'}),
            'session_year': forms.TextInput(attrs={'class': 'form-control'}),
            'holiday_name': forms.TextInput(attrs={'class': 'form-control'}),
            'holiday_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'from_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'to_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def save(self, commit=True):
        holiday = super().save(commit=False)
        if commit:
            holiday.save()
            self.save_m2m()  # This ensures the ManyToManyField values are saved
        return holiday
