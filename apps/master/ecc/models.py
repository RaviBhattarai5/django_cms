from django.db import models

class ECCMaster(models.Model):
    weight_from = models.DecimalField(max_digits=18, decimal_places=2)
    weight_to = models.DecimalField(max_digits=18, decimal_places=2)
    serial_no = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.serial_no}: {self.weight_from} - {self.weight_to} (Active: {self.is_active})"
