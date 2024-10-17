from django.db import models
from django.contrib.auth.models import User
from apps.master.pick_list.models import PickList
from django.utils import timezone

class FmsStage(models.Model):
    fms_stage_name = models.CharField(max_length=50) 
    tat_mode = models.ForeignKey(PickList, on_delete=models.CASCADE, null=True)  
    tat_value = models.FloatField()  
    serial_no = models.IntegerField()  
    is_active = models.BooleanField(default=True)  

    created_by = models.ForeignKey(User, related_name='fms_stages_created', on_delete=models.CASCADE, null=True, blank=True)  
    created_date = models.DateTimeField(auto_now_add=True) 

    updated_by = models.ForeignKey(User, related_name='fms_stages_updated', on_delete=models.CASCADE, null=True, blank=True)  
    updated_date = models.DateTimeField(auto_now=True) 

    deleted_by = models.ForeignKey(User, related_name='fms_stages_deleted', on_delete=models.CASCADE, null=True, blank=True)  
    deleted_date = models.DateTimeField(null=True, blank=True) 
    
    rv = models.BinaryField()  

    is_deleted = models.BooleanField(default=False)
    

    def delete(self, *args, **kwargs):
        """Soft delete: mark the record as deleted instead of removing it from the database."""
        self.is_deleted = True
        self.deleted_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.fms_stage_name
    
    def save(self, *args, **kwargs):
        """Automatically set the created_date or updated_date."""
        if not self.pk:
            self.created_date = timezone.now()
        else:
            self.updated_date = timezone.now() 
        super().save(*args, **kwargs)

