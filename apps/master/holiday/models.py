from django.db import models
from django.contrib.auth.models import User  
holiday_type=[
        ('Public', 'Public Holiday'),
        ('Optional', 'Optional Holiday'),
        ('Religious', 'Religious Holiday'),
        ('National', 'National Holiday'),
    ]
class Holidays(models.Model):
    sessionYr = models.CharField(max_length=10, verbose_name="Session Year")  
    holiday_Name = models.CharField(max_length=255, verbose_name="Holiday Name")  
    holiday_date = models.DateField(verbose_name="Holiday Date") 
    from_date = models.DateField(verbose_name="From Date", null=True, blank=True)
    to_date = models.DateField(verbose_name="To Date", null=True, blank=True) 
    holidayType = models.CharField(max_length=50,choices=holiday_type, verbose_name="Holiday Type")  
    is_active = models.BooleanField(default=True, verbose_name="Is Active") 
    createdBY = models.ForeignKey(User, on_delete=models.CASCADE, related_name='holidays_created', verbose_name="Created By")  
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")  
    update_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='holidays_updated', verbose_name="Updated By")  
    update_date = models.DateTimeField(auto_now=True, verbose_name="Updated Date") 
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='holidays_deleted', verbose_name="Deleted By") 
    deleted_date = models.DateTimeField(null=True, blank=True, verbose_name="Deleted Date")  

    class Meta:
        verbose_name = "Holiday"
        verbose_name_plural = "Holidays"
        ordering = ['holiday_date'] 

    def __str__(self):
        return f"{self.holiday_Name} ({self.sessionYr})" 
