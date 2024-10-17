from django.db import models
from apps.master.country.models import Country
from apps.administrator.users.models import User

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='states')
    state_code = models.CharField(max_length=10)  
    state_name = models.CharField(max_length=100) 
    capital_name = models.CharField(max_length=100)  
    disable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')  
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='updated_by', blank=True, null=True)  
    updated_at = models.DateTimeField(blank=True, null=True)

   

    def __str__(self):
        return self.state_name