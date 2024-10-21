from django.contrib import admin
from .models import UserRole
# Register your models here.
@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display=['id', 'user', 'role']