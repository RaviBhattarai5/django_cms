from django.db import models
from apps.master.state.models import State
choice_field=(
    ('HO', 'Head Office'), 
    ('BR', 'Branch')
)
class MasterBranch(models.Model):  
    title = models.CharField(max_length=200)  
    email = models.EmailField(unique=True)  
    disable = models.BooleanField(default=False)  
    code = models.CharField(max_length=50)  
    brAddress = models.CharField(max_length=255)  
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='entities') 
    brType = models.CharField(max_length=2, choices=choice_field)  
    isDealer = models.BooleanField(default=False)  
    contactNo = models.CharField(max_length=15)  
    isOTPValidation = models.BooleanField(default=False) 

    def __str__(self):
        return str(self.id)
