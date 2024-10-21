from django import forms
from .models import PlanningActivity


class PlanningActivityForm(forms.ModelForm):
    class Meta:
        model = PlanningActivity
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'title'}),
            'category' : forms.Select(attrs={'class':'form-select', 'id': 'category'}),
            'disable': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'disable'}),
            }