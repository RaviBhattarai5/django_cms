from django.urls import path
from .views import get_sheet_data, InterestedSheetListView

urlpatterns = [
    path('', InterestedSheetListView.as_view(), name='sheet_data'),
]
