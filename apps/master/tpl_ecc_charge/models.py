from django.db import models
from django.contrib.auth.models import User 
from apps.master.transporter.models import Transporter
from apps.master.ecc.models import ECCMaster
class EccTransaction(models.Model):
    transporter = models.ForeignKey(Transporter, on_delete=models.CASCADE, null=True, blank=True, )  
    ecc = models.ForeignKey(ECCMaster, on_delete=models.CASCADE, null=True, blank=True)  
    amount = models.DecimalField(max_digits=18, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,  blank=True, related_name='ecc_transaction_created_by')
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='ecc_transaction_updated_by')
    updated_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    rv = models.DateTimeField(auto_now=True, null=True, blank=True)  

    # def __str__(self):
    #     return f"Transaction {self.id} for Transporter {self.transporter}"

    def __str__(self):
        return self.ecc or 'Unnamed ECC'