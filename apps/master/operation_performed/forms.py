from django import forms
from .models import OperationPerformed


class OperationPerformedForm(forms.ModelForm):
    class Meta:
        model = OperationPerformed
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'title'}),
            'disable': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'disable'}),
            }