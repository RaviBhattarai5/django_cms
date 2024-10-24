from django.db import models

class ECCMaster(models.Model):
    weight_from = models.DecimalField(max_digits=18, decimal_places=2)
    weight_to = models.DecimalField(max_digits=18, decimal_places=2)
    serial_no = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"(serial No -{self.serial_no}):(weight_From - {self.weight_from}) - (Weight_To - {self.weight_to}) "
