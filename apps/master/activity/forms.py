from django import forms
from .models import Activity


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'
        widgets = {
            'activity_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'activity_title'}),
            'plus_minus': forms.Select(attrs={'class': 'form-select', 'id': 'plus_minus'}),
            }