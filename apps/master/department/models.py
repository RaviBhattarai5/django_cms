from django.db import models


# Create your models here.
class Department(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "master_department"

    def __str__(self):
        return self.title
