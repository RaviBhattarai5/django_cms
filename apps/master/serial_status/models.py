from django.db import models

class SerialStatus(models.Model):
    serialStatus = models.CharField(max_length=255, null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.serialStatus
