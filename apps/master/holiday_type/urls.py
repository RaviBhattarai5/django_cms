from django.urls import path
from .views import *
urlpatterns = [
    path('', HolidayTypeListView.as_view(), name='holiday_type_list'),
    path('create/', HolidaysTypeCreateView.as_view(), name='holiday_type_create'),
    # path('<int:pk>/', GroupDetailView.as_view(), name='holiday_type_detail'),
    path('<int:pk>/update/', HolidaysTypeUpdateView.as_view(), name='holiday_type_update'),
    path('<int:pk>/delete/', HolidaysTypeDeleteView.as_view(), name='holiday_type_delete'),
]
