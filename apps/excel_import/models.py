from django.db import models

# Create your models here.
class ImportTest(models.Model):
    first_name = models.CharField(max_length=255);
    last_name = models.CharField(max_length=255);
    email = models.CharField(max_length=255);
    age = models.IntegerField();
    
    def __str__(self):
        return self.first_name
    
    