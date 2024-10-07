from django.db import models


# Create your models here.
class PlanningActivityCategory(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "master_planning_activity_category"

    def __str__(self):
        return self.title
