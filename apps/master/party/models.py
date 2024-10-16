from django.db import models
from apps.administrator.users.models import User
from apps.master.area.models import Area
from apps.master.pick_list.models import PickList
from apps.master.state.models import State
from apps.master.city.models import City

# Create your models here.


class Party(models.Model):
    contact_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    area = models.ForeignKey(
        Area, on_delete=models.CASCADE, related_name="party_area", blank=True, null=True
    )

    mobile_no = models.CharField(max_length=15, blank=True, null=True)
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    credit_days = models.IntegerField(blank=True, null=True)
    payment_mode = models.ForeignKey(
        PickList,
        on_delete=models.CASCADE,
        related_name="party_payment_mode",
        blank=True,
        null=True,
    )
    disable = models.BooleanField(default=False)
    gst_no = models.CharField(max_length=255, blank=True, null=True)
    pan_no = models.CharField(max_length=255, blank=True, null=True)
    credit_limit = models.DecimalField(
        max_digits=18, decimal_places=2, blank=True, null=True
    )
    pin_code = models.CharField(max_length=6, blank=True, null=True)
    state = models.ForeignKey(
        State,
        on_delete=models.CASCADE,
        related_name="party_state",
        blank=True,
        null=True,
    )
    city = models.ForeignKey(
        City, on_delete=models.CASCADE, related_name="party_city", blank=True, null=True
    )
    client_code = models.CharField(max_length=20, blank=True, null=True)
    is_tcs_available = models.BooleanField(default=False)
    adv_pdc_cdc = models.ForeignKey(
        PickList,
        on_delete=models.CASCADE,
        related_name="party_Adv_Pdc_Cdc",
        blank=True,
        null=True,
    )
    security_cheque = models.ForeignKey(
        PickList,
        on_delete=models.CASCADE,
        related_name="party_security_cheque",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="party_created_by", blank=True, null=True
    )
    updated_at = models.DateTimeField(blank=True, null=True)
    updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="party_updated_by",
        blank=True,
        null=True,
    )
    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="party_deleted_by",
        blank=True,
        null=True,
    )

    class Meta:
        db_table = "master_party"

    def __str__(self):
        return self.name
