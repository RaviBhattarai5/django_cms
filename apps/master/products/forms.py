from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            'product_name',
            'product_code',
            'description',
            # 'selling_price',
            # 'max_selling_price',
            # 'min_discount',
            'group',
            'serial_status',
            'warranty',
            # 'created_by',
            # 'updated_by',
            'disable',
            # 'tran_limit',
            # 'gst',
            # 'cgst',
            # 'sgst',
            'weight_kg',
            'volumetric_weight',
            'moq',
            # 'transfer_price'
        ]
        
        # Optionally, you can add widgets to customize field renderings:
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'product_code': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_status': forms.Select(attrs={'class': 'form-select'}),
            'moq': forms.NumberInput(attrs={'class': 'form-control'}),
            'group': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'selling_price': forms.NumberInput(attrs={'step': 0.01, 'class': 'form-control'}),
            'max_selling_price': forms.NumberInput(attrs={'step': 0.01, 'class': 'form-control'}),
            'min_discount': forms.NumberInput(attrs={'min': 0, 'class': 'form-control'}),
            'warranty': forms.NumberInput(attrs={'min': 0, 'class': 'form-control'}),
            'weight_kg': forms.NumberInput(attrs={'step': 0.01, 'class': 'form-control'}),
            'volumetric_weight': forms.NumberInput(attrs={'step': 0.01, 'class': 'form-control'}),
            'tran_limit': forms.NumberInput(attrs={'step': 0.01, 'class': 'form-control'}),
            'gst': forms.NumberInput(attrs={'step': 0.01, 'class': 'form-control'}),
            'cgst': forms.NumberInput(attrs={'step': 0.01, 'class': 'form-control'}),
            'sgst': forms.NumberInput(attrs={'step': 0.01, 'class': 'form-control'}),
        }

        
        # Optional: customize the form labels
        labels = {
            'product_name': 'Product Name',
            'product_code': 'Product Code',
            'description': 'Description',
            'selling_price': 'Selling Price',
            'max_selling_price': 'Maximum Selling Price',
            'min_discount': 'Minimum Discount',
            'group': 'Product Group',
            'serial_status': 'Serial Status',
            'warranty': 'Warranty (months)',
            'disable': 'Disable Product',
            'tran_limit': 'Transaction Limit',
            'gst': 'GST',
            'cgst': 'Central GST (CGST)',
            'sgst': 'State GST (SGST)',
            'weight_kg': 'Weight (kg)',
            'volumetric_weight': 'Volumetric Weight',
            'moq': 'Minimum Order Quantity (MOQ)',
            'transfer_price': 'Transfer Price',
        }
        
    # Optional: Custom validation for fields if needed
    def clean_min_discount(self):
        min_discount = self.cleaned_data.get('min_discount')
        if min_discount < 0:
            raise forms.ValidationError("Minimum discount cannot be negative.")
        return min_discount

    def clean_weight_kg(self):
        weight_kg = self.cleaned_data.get('weight_kg')
        if weight_kg < 0:
            raise forms.ValidationError("Weight cannot be negative.")
        return weight_kg
