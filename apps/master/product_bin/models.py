from django.db import models

class ProductBin(models.Model):  
    title = models.CharField(max_length=200)  
    disable = models.BooleanField(default=False)  
    serialNo = models.IntegerField()  

    def __str__(self):
        return self.title
