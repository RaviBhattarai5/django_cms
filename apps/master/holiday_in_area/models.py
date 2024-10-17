from django.db import models
from apps.master.holiday.models import Holidays
from apps.master.area.models import Area

class HolidayInArea(models.Model):
    holiday_id = models.ForeignKey(Holidays, on_delete=models.CASCADE)
    area_id = models.ForeignKey(Area, on_delete=models.CASCADE)                  
    is_active = models.BooleanField(default=True)    

    class Meta:
        verbose_name = "Holiday"
        verbose_name_plural = "Holidays"

    def __str__(self):
        return f"Holiday {self.holiday_id} in Area {self.area_id}"
