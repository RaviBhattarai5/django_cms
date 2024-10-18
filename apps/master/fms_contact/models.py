from django.db import models
from django.contrib.auth.models import User
from apps.master.area.models import Area
from apps.master.fms_stage.models import FmsStage

class FmsContact(models.Model):
    id = models.AutoField(primary_key=True)  # FK
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)  # FK to Area
    fms_stage = models.ForeignKey(FmsStage, on_delete=models.SET_NULL, null=True)  # FK to FmsStage

    contact_name = models.CharField(max_length=200)  # varchar(200)
    contact_no = models.CharField(max_length=10)  # varchar(10)
    email_id = models.EmailField(max_length=200)  # varchar(200)

    is_active = models.BooleanField(default=True)  # boolean

    created_by = models.ForeignKey(User, related_name='fms_contacts_created', on_delete=models.SET_NULL, null=True, blank=True)  # FK to User
    created_date = models.DateTimeField(auto_now_add=True)  # datetime

    updated_by = models.ForeignKey(User, related_name='fms_contacts_updated', on_delete=models.SET_NULL, null=True, blank=True)  # FK to User
    updated_date = models.DateTimeField(auto_now=True)  # datetime

    deleted_by = models.ForeignKey(User, related_name='fms_contacts_deleted', on_delete=models.SET_NULL, null=True, blank=True)  # FK to User
    deleted_date = models.DateTimeField(null=True, blank=True)  # datetime

    rv = models.BinaryField()  # timestamp (for row versioning, typically handled by the database)

    def __str__(self):
        return self.contact_name
