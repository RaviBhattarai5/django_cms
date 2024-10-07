from django import forms
from .models import ProdutCategory

class ProdutCategoryForm(forms.ModelForm):
    class Meta:
        model = ProdutCategory
        fields = ['title', 'disable',]  

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'disable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  
        }

        labels = {
            'title': 'Title',
            'disable': 'Disable',
        }
