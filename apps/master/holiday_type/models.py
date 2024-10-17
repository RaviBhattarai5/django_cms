from django.db import models

class HolidaysType(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    holidays_type = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.name

