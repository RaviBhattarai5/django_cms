from django.urls import path
from .views import set_permission_view

urlpatterns = [
    path('', set_permission_view, name='set_permission'),
]
