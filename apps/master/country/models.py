from django.db import models


class Country(models.Model):  
    name = models.CharField(max_length=100)  
    shortName = models.CharField(max_length=10)
    code = models.CharField(max_length=20)  
    currency = models.CharField(max_length=50)  
    order = models.IntegerField() 
    disable = models.BooleanField(default=False) 

    def __str__(self):
        return str(self.id)

