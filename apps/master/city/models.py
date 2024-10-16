from django.db import models
from apps.master.state.models import State
from apps.administrator.users.models import User

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    disable = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='city_created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='city_updated_by')
    updated_at = models.DateTimeField(auto_now=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='city_deleted_by')
    deleted_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'master_city'
        
    def __str__(self):
        return self.name