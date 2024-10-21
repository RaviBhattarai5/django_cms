from django import forms
from .models import ProdutCategory

class ProdutCategoryForm(forms.ModelForm):
    class Meta:
        model = ProdutCategory
        fields = [
            'category_name', 
            'is_active', 
            'created_by', 
            'updated_by', 
            'deleted_by', 
            'updated_date', 
            'deleted_date'
        ]
        widgets = {
            'category_name':forms.TextInput(attrs={'class':'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'updated_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'deleted_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    labels={
        'category_name':'Category Name'
    }
