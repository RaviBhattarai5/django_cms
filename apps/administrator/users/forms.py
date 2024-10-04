from django import forms
from django.contrib.auth.models import User
from apps.administrator.roles.models import Roles
from apps.administrator.users.models import UserRole

class UserForm(forms.ModelForm):
    roles = forms.ModelMultipleChoiceField(
        queryset=Roles.objects.exclude(isRole=False).all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control js-example-basic-multiple'}),  # Use checkboxes, or use forms.SelectMultiple for a dropdown
        required=False
    )
    password=forms.CharField(label="Password", required=False,  widget=forms.PasswordInput( attrs={'class':"form-control"}))


    
    class Meta:
        model = User
        fields = ['roles','username', 'first_name', 'last_name', 'email', 'password','is_active']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            # 'password': forms.PasswordInput(attrs={'class': 'form-control', 'required':False}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
    def __init__(self, *args, **kwargs):
        user_instance = kwargs.pop('user_instance', None)
        super().__init__(*args, **kwargs)
        if user_instance:
            self.fields['roles'].initial = user_instance.userrole_set.values_list('role', flat=True)
            self.fields['password'].required = False
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password']) 
        if commit:
            user.save()
            UserRole.objects.filter(user=user).delete()
            for role in self.cleaned_data['roles']:
                UserRole.objects.create(user=user, role=role)
        return user