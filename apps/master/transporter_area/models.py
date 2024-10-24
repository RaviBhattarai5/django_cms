from django.db import models
from apps.master.transporter.models import Transporter
from apps.master.city.models import City
class TransporterArea(models.Model):
    id = models.AutoField(primary_key=True)
    transporter = models.ForeignKey(Transporter, on_delete=models.CASCADE, related_name='transporter_areas')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='transporter_areas')
    min_weight = models.DecimalField(max_digits=18, decimal_places=2)
    min_charge = models.DecimalField(max_digits=18, decimal_places=2)
    tpt_charge = models.DecimalField(max_digits=18, decimal_places=2)
    ecc_charge = models.DecimalField(max_digits=18, decimal_places=2)
    fuel_surcharge = models.DecimalField(max_digits=18, decimal_places=2)
    currency_adjustment_factor = models.DecimalField(max_digits=18, decimal_places=2)
    docket_fees = models.DecimalField(max_digits=18, decimal_places=2)
    rov = models.DecimalField(max_digits=18, decimal_places=2)
    mcc = models.DecimalField(max_digits=18, decimal_places=2)
    oda = models.DecimalField(max_digits=18, decimal_places=2)
    ss = models.DecimalField(max_digits=18, decimal_places=2)
    annual_hike = models.DecimalField(max_digits=18, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='created_transporter_areas')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.IntegerField(null=True, blank=True,)  # Assuming this is an integer representing user ID
    updated_date = models.DateTimeField(auto_now=True, blank=True,)
    rv = models.DateTimeField(auto_now_add=True, blank=True,)  # Assuming you want a timestamp for record versioning

    def __str__(self):
        return f"Transporter Area {self.id} - {self.city} for Transporter {self.transporter}"
