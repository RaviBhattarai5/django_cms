from django.db import models
from django.contrib.auth.models import User  
from apps.master.area.models import Area
from django.utils import timezone

class Transporter(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    transporter_name = models.CharField(max_length=200, blank=True, null=True)
    gst_no = models.CharField(max_length=15, blank=True, null=True)
    mobile_no1 = models.CharField(max_length=10, blank=True, null=True)
    mobile_no2 = models.CharField(max_length=10, blank=True, null=True)  # Optional second mobile number
    tracking_url = models.URLField(max_length=1000, blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='transporter_created_by')
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='transporter_updated_by')
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    deleted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='transporter_deleted_by')
    deleted_date = models.DateTimeField(null=True, blank=True)
    rv = models.DateTimeField(auto_now=True, blank=True, null=True)  
    min_weight_charge = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    min_weight = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    min_charge = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    tpt_charge = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)

    is_delete=models.BooleanField(default=False)

    # def __str__(self):
    #     return self.transporter_name
    
    def __str__(self):
        return self.transporter_name or 'Unnamed Transporter'  # Ensure it returns a string


    def delete(self, *args, **kwargs):
        """Soft delete: mark the record as deleted instead of removing it from the database."""
        self.is_deleted = True
        self.deleted_date = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        """Automatically set the created_date or updated_date."""
        if not self.pk:
            self.created_date = timezone.now()
        else:
            self.updated_date = timezone.now() 
        super().save(*args, **kwargs)