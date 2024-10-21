from django.urls import path
from . import views

urlpatterns = [
    path('', views.import_excel, name='import_excel'),
]