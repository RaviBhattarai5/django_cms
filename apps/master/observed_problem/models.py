from django.db import models


# Create your models here.
class ObservedProblem(models.Model):
    title = models.CharField(max_length=255)
    disable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "master_observed_problem"

    def __str__(self):
        return self.title
