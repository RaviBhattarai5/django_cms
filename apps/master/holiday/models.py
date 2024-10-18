# models.py
from django.db import models
from django.contrib.auth.models import User  
from django.utils import timezone
from apps.master.holiday_type.models import HolidaysType
from apps.master.area.models import Area

class Holidays(models.Model):
    session_year = models.CharField(max_length=10, verbose_name="Session Year", null=True, blank=True)  
    holiday_name = models.CharField(max_length=255, verbose_name="Holiday Name", error_messages={'required': 'Holiday name is required.'})  
    holiday_date = models.DateField(verbose_name="Holiday Date", null=True) 
    from_date = models.DateField(verbose_name="From Date", null=True, blank=True)
    to_date = models.DateField(verbose_name="To Date", null=True, blank=True) 
    holiday_type = models.ForeignKey(HolidaysType, on_delete=models.CASCADE, default=True, related_name='holiday', verbose_name="Holiday Type")  
    
    # Changed to ManyToManyField to allow selecting multiple areas
    holiday_in_area = models.ManyToManyField(Area, verbose_name="Holiday in Area", blank=True)

    is_active = models.BooleanField(default=True, verbose_name="Is Active") 
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='holidays_created', verbose_name="Created By")  
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")  
    update_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='holidays_updated', verbose_name="Updated By")  
    update_date = models.DateTimeField(auto_now=True, verbose_name="Updated Date") 
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='holidays_deleted', verbose_name="Deleted By") 
    deleted_date = models.DateTimeField(null=True, blank=True, verbose_name="Deleted Date")  

    is_delete = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Holiday"
        verbose_name_plural = "Holidays"
        ordering = ['holiday_date']

    def delete(self, *args, **kwargs):
        self.is_delete = True  
        self.deleted_date = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.holiday_name} ({self.session_year})"

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_date = timezone.now()
        else:
            self.update_date = timezone.now()
        super().save(*args, **kwargs)
