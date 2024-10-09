from django.urls import path
from .views import get_sheet_data

urlpatterns = [
    path('', get_sheet_data, name='sheet_data'),
]
