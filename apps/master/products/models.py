from django.db import models
from apps.master.group.models import MasterGroup
from apps.master.serial_status.models import SerialStatus
from django.contrib.auth.models import User
from django.utils import timezone

class Products(models.Model):
    product_name = models.CharField(max_length=200, )  
    product_code = models.CharField(max_length=100)  
    description = models.TextField(blank=True, null=True)  
    
    selling_price = models.DecimalField(max_digits=18, decimal_places=2, null=True)  
    max_selling_price = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    min_discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    group = models.ForeignKey(MasterGroup, on_delete=models.CASCADE, null=True, blank=True)  
    serial_status = models.ForeignKey(SerialStatus, on_delete=models.CASCADE, null=True, blank=True) 
    
    warranty = models.PositiveIntegerField(null=True)  
    
    # Created/Updated/Deleted info
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='product_created')
    created_date = models.DateTimeField(default=timezone.now)  
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='product_updated')
    updated_date = models.DateTimeField(null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='product_deleted')
    deleted_date = models.DateTimeField(null=True, blank=True)
    
    # Boolean for enabling/disabling the product
    disable = models.BooleanField(default=True)
    
    # Financial fields
    tran_limit = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    gst = models.DecimalField(max_digits=18, decimal_places=2, null=True)  
    cgst = models.DecimalField(max_digits=18, decimal_places=2, null=True)  
    sgst = models.DecimalField(max_digits=18, decimal_places=2, null=True)  
    
    # Physical attributes
    weight_kg = models.DecimalField(max_digits=10, decimal_places=2)  
    volumetric_weight = models.DecimalField(max_digits=18, decimal_places=2)  
    
    moq = models.PositiveIntegerField()  
    transfer_price = models.DecimalField(max_digits=18, decimal_places=2, null=True ) 
    
    is_deleted = models.BooleanField(default=False)
    
    def delete(self, *args, **kwargs):
        """Soft delete: mark the record as deleted instead of removing it from the database."""
        self.is_deleted = True
        self.deleted_date = timezone.now()
        self.save()

    def __str__(self):
        return self.product_name 

    def save(self, *args, **kwargs):
        """Automatically set the created_date or updated_date."""
        if not self.pk:
            self.created_date = timezone.now()
        else:
            self.updated_date = timezone.now() 
        super().save(*args, **kwargs)
