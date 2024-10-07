from django import forms
from .models import ProductGroup

class ProductGroupForm(forms.ModelForm):
    class Meta:
        model = ProductGroup
        fields = ['title', 'categoryId', 'disable'] 

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'categoryId': forms.Select(attrs={'class': 'form-control'}),  
            'disable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  
        }

      
        labels = {
            'title': 'Product Title',
            'categoryId': 'Product Category',
            'disable': 'Disable',
        }
