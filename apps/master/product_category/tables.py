# tables.py
import django_tables2 as tables
from .models import ProdutCategory

class ProdutCategoryTable(tables.Table):
    class Meta:
        model = ProdutCategory
        fields = ("id", "category_name", "is_active", "created_by", "updated_by", "created_date", "updated_date")  # Add other fields as needed
        attrs = {'class': 'table'}  # Optional: add classes to the table for styling
