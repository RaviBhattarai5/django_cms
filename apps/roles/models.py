from django.db import models
class Roles(models.Model):
    role_name=models.CharField(max_length=100)
    descriptions=models.TextField()
    isRole = models.BooleanField(default=False, verbose_name='isRole')