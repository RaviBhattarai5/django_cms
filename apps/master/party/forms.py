from django import forms
from .models import Party
from apps.master.pick_list.models import PickList
from utils.common import set_picklist_querysets


class PartyForm(forms.ModelForm):

    class Meta:
        model = Party
        fields = "__all__"

        widgets = {
            "contact_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": ""}
            ),
            "company_name": forms.TextInput(attrs={"class": "form-control"}),
            "area": forms.Select(attrs={"class": "form-select"}),
            "mobile_no": forms.TextInput(attrs={"class": "form-control"}),
            "phone_no": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(
                attrs={"class": "form-control", "required": False}
            ),
            "credit_days": forms.NumberInput(attrs={"class": "form-control"}),
            "payment_mode": forms.Select(attrs={"class": "form-select"}),
            "disable": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "gst_no": forms.TextInput(attrs={"class": "form-control"}),
            "pan_no": forms.TextInput(attrs={"class": "form-control"}),
            "credit_limit": forms.NumberInput(
                attrs={"class": "form-control", "step": "any"}
            ),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "pin_code": forms.TextInput(attrs={"class": "form-control"}),
            "state": forms.Select(attrs={"class": "form-select"}),
            "city": forms.Select(attrs={"class": "form-select"}),
            "client_code": forms.TextInput(attrs={"class": "form-control"}),
            "is_tcs_available": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
            "adv_pdc_cdc": forms.Select(attrs={"class": "form-select"}),
            "security_cheque": forms.Select(attrs={"class": "form-select"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields_to_set = {
            "adv_pdc_cdc": "PDC_ADV_CDC",
            "payment_mode": "PAYMENT_MODE",
            "security_cheque": "SECURITY_CHEQUE",
        }
        set_picklist_querysets(self.fields, fields_to_set)
       