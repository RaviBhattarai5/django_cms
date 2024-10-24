from django.db import models
from django.contrib.auth.models import User
from apps.master.enquiry_stage.models import EnquiryStage

class EnquiryStatus(models.Model):
    case_study = models.CharField(max_length=50, blank=True, null=True)
    enquiry_status_name = models.CharField(max_length=60, blank=True, null=True)
    enquiry_stage_id = models.ForeignKey(EnquiryStage, on_delete=models.CASCADE, related_name='enquiry_statuses', blank=True, null=True)
    remarks = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='created_enquiry_statuses', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='updated_enquiry_statuses', blank=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    rv = models.DateTimeField(auto_now=True, blank=True, null=True)  # Django does not have a timestamp field, using DateTimeField with auto_now

    def __str__(self):
        return self.EnquiryStatusName
