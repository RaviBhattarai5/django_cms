from django.contrib import admin

# Register your models here.
from .models import Roles
@admin.register(Roles)
class Student(admin.ModelAdmin):
    list_display=['id']