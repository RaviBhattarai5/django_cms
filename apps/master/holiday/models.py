from django.db import models
from django.contrib.auth.models import User  
from django.utils import timezone

holiday_type=[
        ('Public', 'Public Holiday'),
        ('Optional', 'Optional Holiday'),
        ('Religious', 'Religious Holiday'),
        ('National', 'National Holiday'),
    ]

class Holidays(models.Model):
    session_year = models.CharField(max_length=10, verbose_name="Session Year", null=True)  
    holiday_name = models.CharField(max_length=255, verbose_name="Holiday Name" , error_messages={'required': 'Holiday name is required.'})  
    holiday_date = models.DateField(verbose_name="Holiday Date", null=True) 
    from_date = models.DateField(verbose_name="From Date", null=True, blank=True)
    to_date = models.DateField(verbose_name="To Date", null=True, blank=True) 
    holiday_type = models.CharField(max_length=50,choices=holiday_type, verbose_name="Holiday Type")  
    is_active = models.BooleanField(default=True, verbose_name="Is Active") 
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='holidays_created', verbose_name="Created By")  
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")  
    update_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='holidays_updated', verbose_name="Updated By")  
    update_date = models.DateTimeField(auto_now=True, verbose_name="Updated Date") 
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='holidays_deleted', verbose_name="Deleted By") 
    deleted_date = models.DateTimeField(null=True, blank=True, verbose_name="Deleted Date")  

    is_delete=models.BooleanField(default=False)
    class Meta:
        verbose_name = "Holiday"
        verbose_name_plural = "Holidays"
        ordering = ['holiday_date'] 

    def __str__(self):
        return f"{self.holiday_Name} ({self.sessionYr})" 

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

