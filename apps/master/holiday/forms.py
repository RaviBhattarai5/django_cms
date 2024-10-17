from django import forms
from .models import Holidays
from apps.master.area.models import Area

class HolidaysForm(forms.ModelForm):
    # Corrected queryset for holiday_in_area field to query `Area` instead of `Holidays`
    holiday_in_area = forms.ModelMultipleChoiceField(
        queryset=Area.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control js-example-basic-multiple'}),  # Multiple select for the field
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

    def __init__(self, *args, **kwargs):
        user_instance = kwargs.pop('user_instance', None)
        super().__init__(*args, **kwargs)
        if user_instance:
            # Set initial values based on user_instance for holiday_in_area
            self.fields['holiday_in_area'].initial = user_instance.holidays_set.values_list('holiday_in_area', flat=True).first()

    def save(self, commit=True):
        holiday = super().save(commit=False)
        # Additional logic before saving
        if commit:
            holiday.save()
        return holiday
