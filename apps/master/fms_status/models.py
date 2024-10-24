from django.db import models
from django.contrib.auth.models import User  # Assuming FK fields reference the User model

class FmsStatus(models.Model):

    
    fms_action_type = models.CharField(max_length=20, null=True, blank=True)
    fms_status_code = models.CharField(max_length=50, null=True, blank=True)
    fms_status_name = models.CharField(max_length=50, null=True, blank=True)
    
    parent_id = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='children')
    serial_no = models.IntegerField(null=True, blank=True)
    
    is_active = models.BooleanField(default=True, null=True, blank=True)
    
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_statuses')
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='updated_statuses')
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='deleted_statuses')
    deleted_date = models.DateTimeField(null=True, blank=True)
    
    RV = models.DateTimeField(auto_now=True)  # Using DateTimeField for timestamp

    def __str__(self):
        return self.fms_status_name
