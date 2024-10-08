from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'productCode', 'hsnCode']  

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product title'}),
            'productCode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product code'}),
            'hsnCode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter HSN code'}),
        }

        labels = {
            'title': 'Product Title',
            'productCode': 'Product Code',
            'hsnCode': 'HSN Code',
        }
