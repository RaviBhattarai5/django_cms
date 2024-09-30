from django.db import models
from apps.menu.models import Menu
from apps.roles.models import Roles
from apps.permission_type.models import PermissionType

class SetPermission(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    permission_type = models.ForeignKey(PermissionType, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('menu', 'role', 'permission_type')
