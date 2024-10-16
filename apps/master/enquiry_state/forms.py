from django import forms
from .models import EnquiryState


class EnquiryStateForm(forms.ModelForm):
    class Meta:
        model = EnquiryState
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "id": "title"}),
            "disable": forms.CheckboxInput(
                attrs={"class": "form-check-input", "id": "disable"}
            ),
        }
