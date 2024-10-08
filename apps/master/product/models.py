from django.db import models

class Product(models.Model): 
    title = models.CharField(max_length=200)  
    productCode = models.CharField(max_length=100) 
    hsnCode = models.CharField(max_length=50)  

    def __str__(self):
        return self.title
