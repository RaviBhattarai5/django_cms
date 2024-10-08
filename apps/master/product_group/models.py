from django.db import models
from apps.master.product_category.models import ProdutCategory



class ProductGroup(models.Model):  
    title = models.CharField(max_length=200)  
    categoryId = models.ForeignKey(ProdutCategory, on_delete=models.CASCADE, related_name='products')  
    disable = models.BooleanField(default=False)  

    def __str__(self):
        return self.title