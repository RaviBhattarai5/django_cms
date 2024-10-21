from django.db import models
from apps.master.planning_activity_category.models import PlanningActivityCategory


# Create your models here.
class PlanningActivity(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(PlanningActivityCategory, on_delete=models.CASCADE)
    disable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "master_planning_activity"

    def __str__(self):
        return self.title
