from django import forms
from .models import HolidayInArea

from apps.master.holiday_in_area.models import HolidayInArea
from apps.master.area.models import Area

class HolidayInAreaForm(forms.ModelForm):
    class Meta:
        model = HolidayInArea
        fields = ['holiday_id', 'area_id', 'is_active']
        widgets = {
            'holiday_id': forms.Select(attrs={'class': 'form-control'}),
            'area_id': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

