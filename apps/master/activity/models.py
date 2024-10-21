from django.db import models

# Create your models here.

class Activity(models.Model):
    
    PLUS_MINUS_CHOICES = [
        ('+', '+'),
        ('-', '-'),
    ]
    activity_name = models.CharField(max_length=255)
    plus_minus = models.CharField(max_length=5, choices=PLUS_MINUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.activity_name
    
    class Meta:
        db_table = 'master_activity'