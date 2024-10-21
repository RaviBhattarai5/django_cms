from django import forms
from .models import ObservedProblem


class ObservedProblemForm(forms.ModelForm):
    class Meta:
        model = ObservedProblem
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'title'}),
            'disable': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'disable'}),
            }