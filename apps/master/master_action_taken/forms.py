from django import forms
from .models import MasterActionTaken


class MasterActionTakenForm(forms.ModelForm):
    class Meta:
        model = MasterActionTaken
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'title'}),
            'disable': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'disable'}),
            }