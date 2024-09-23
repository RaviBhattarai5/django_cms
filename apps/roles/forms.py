from django import forms
from .models import Roles

class RolesForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = '__all__'
        widgets = {'isRole' : forms.CheckboxInput(attrs={'class':'form-check-input'}) }
