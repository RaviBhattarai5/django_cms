from django.db import models

# Create your models here.
class MasterActionTaken(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    disable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id