from django import forms
from .models import Roles

class RolesForm(forms.ModelForm):
    class Meta:
        model = Roles
        fields = ['role_name', 'descriptions', 'isRole']
        labels = {
            'role_name': "Role Name",
            'descriptions': "descriptions",
            'isRole': 'isActivate',
        }
        widgets={
            'role_name': forms.TextInput(attrs={'class':'form-control'}),
            'descriptions': forms.TextInput(attrs={'class':'form-control'}),
            'isRole': forms.CheckboxInput(attrs={'class':'form-check-input'}),  
        }
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
            
    def clean(self):
        cleaned_data = super().clean()
        role_name = cleaned_data.get("role_name")
        descriptions = cleaned_data.get("descriptions")

        if not role_name:
            self.add_error('role_name', 'Role_name is required.')
        if not descriptions:
            self.add_error('descriptions', 'Description is required.')

        return cleaned_data
