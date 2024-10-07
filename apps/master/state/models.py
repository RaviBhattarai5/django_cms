from django.db import models
from apps.master.country.models import Country
class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='states')
    stateCode = models.CharField(max_length=10)  
    stateName = models.CharField(max_length=100) 
    capitalName = models.CharField(max_length=100)  
    disable = models.BooleanField(default=False)  

    def __str__(self):
        return self.stateName