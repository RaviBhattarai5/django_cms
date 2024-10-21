from django.db import models

class PickList(models.Model):
    id = models.AutoField(primary_key=True)
    pick_list_name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_active = models.BooleanField(default=True)
    serial_no = models.PositiveIntegerField()  

    def __str__(self):
        return self.pick_list_name
