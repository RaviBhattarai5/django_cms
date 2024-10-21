from django import forms
from apps.administrator.roles.models import Roles
from apps.administrator.menu.models import Menu
from apps.administrator.permission_type.models import PermissionType
from .models import SetPermission

class SetPermissionForm(forms.Form):
    role = forms.ModelChoiceField(
        queryset=Roles.objects.exclude(isRole=False).all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Select Role"
    )

    def __init__(self, *args, **kwargs):
        role = kwargs.pop('role', None)
        super(SetPermissionForm, self).__init__(*args, **kwargs)
        
        menus = Menu.objects.all()
        permission_types = PermissionType.objects.all()

        for menu in menus:
            for permission_type in permission_types:
                field_name = f'{menu.id}_{permission_type.id}'
                self.fields[field_name] = forms.BooleanField(
                    required=False,
                    label=f'{menu.title} - {permission_type.name}',
                    initial=False
                )
                if role and SetPermission.objects.filter(role=role, menu=menu, permission_type=permission_type).exists():
                    self.fields[field_name].initial = True
