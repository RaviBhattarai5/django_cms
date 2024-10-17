<<<<<<< HEAD

=======
>>>>>>> 9a65824f0901d2030ba6ad8ffc9603a27a366508
from django.db import models

class HolidaysType(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    holidays_type = models.CharField(max_length=100, null=True)


    def __str__(self):
<<<<<<< HEAD
        return self.name

=======
        return self.name
>>>>>>> 9a65824f0901d2030ba6ad8ffc9603a27a366508
