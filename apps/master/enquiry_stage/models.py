from django.db import models

class EnquiryStage(models.Model):
    enquiry_stage_name = models.CharField(max_length=50)  # Varchar(50)
    serial_no = models.IntegerField()  # Integer field
    is_active = models.BooleanField(default=True)  # Boolean field with default value

    def __str__(self):
        return self.enquiry_stage_name
