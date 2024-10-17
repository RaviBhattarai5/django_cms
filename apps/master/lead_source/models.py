from django.db import models
from django.contrib.auth.models import User

class LeadSource(models.Model):
    lead_source_code = models.CharField(max_length=30)  
    lead_source_name = models.CharField(max_length=100) 
    
    is_lead_generate_by = models.BooleanField(default=False)  
    is_lead_assign_to = models.BooleanField(default=False)  
    is_re_generate_by = models.BooleanField(default=False)  
    is_re_assign_to = models.BooleanField(default=False)  
    is_lead_created_by = models.BooleanField(default=False)  
    is_active = models.BooleanField(default=True)  

    created_by = models.ForeignKey(User, related_name='lead_sources_created', on_delete=models.CASCADE, null=True, blank=True)  # FK
    created_date = models.DateTimeField(auto_now_add=True) 
    updated_by = models.ForeignKey(User, related_name='lead_sources_updated', on_delete=models.CASCADE, null=True, blank=True)  # FK
    updated_date = models.DateTimeField(auto_now=True) 
    
    user = models.ForeignKey(User, related_name='lead_sources_user', on_delete=models.CASCADE, null=True)  # FK
    
    rv = models.BinaryField() 
    
    def __str__(self):
        return self.lead_source_name
