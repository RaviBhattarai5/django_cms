from django.db import models
from apps.administrator.users.models import User
from apps.master.state.models import State
from apps.master.city.models import City

# Create your models here.

class Area(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    disable = models.BooleanField(default=False)
    has_go_down = models.BooleanField(default=False)
    sr_email = models.CharField(max_length=255, blank=True, null=True)
    gst_no = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    area_code = models.CharField(max_length=255, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='area_state', blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='area_city', blank=True, null=True)
    pin_code = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='area_created_by', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, related_name='area_updated_by', blank=True, null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey(User, related_name='area_deleted_by', blank=True, null=True, on_delete=models.CASCADE)
    deleted_at = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        db_table = 'master_area'
    def __str__(self):
        return self.name