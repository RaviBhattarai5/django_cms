from django import forms
from .models import PlanningActivityCategory


class PlanningActivityCategoryForm(forms.ModelForm):
    class Meta:
        model = PlanningActivityCategory
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'title'}),
            }