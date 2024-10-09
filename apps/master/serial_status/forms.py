from django import forms
from .models import SerialStatus

class SerialStatusForm(forms.ModelForm):
    class Meta:
        model = SerialStatus
        fields = ['serialStatus']  
        widgets = {
            'serialStatus': forms.TextInput(attrs={'placeholder': 'Enter serial status', 'class': 'form-control'}),
        }
