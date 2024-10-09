from django.db import models
from django.contrib.auth.models import User
from apps.master.product_category.models import ProdutCategory

from django.utils import timezone

class MasterGroup(models.Model):
    group_name = models.CharField(max_length=255)
    category_id = models.ForeignKey(ProdutCategory, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='created')
    created_date = models.DateTimeField(null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='updated')
    updated_date = models.DateTimeField(null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='deleted')
    deleted_date = models.DateTimeField(null=True, blank=True)
    
    created_at=models.DateTimeField(auto_now_add=True)

    is_deleted = models.BooleanField(default=False)
    
    def delete(self, *args, **kwargs):
        """Soft delete: mark the record as deleted instead of removing it from the database."""
        self.is_deleted = True
        self.deleted_date = timezone.now()
        self.save()

    def __str__(self):
        return self.group_name

    def save(self, *args, **kwargs):
        """Automatically set the created_date or updated_date."""
        if not self.pk:
            self.created_date = timezone.now()
        else:
            self.updated_date = timezone.now() 
        super().save(*args, **kwargs)