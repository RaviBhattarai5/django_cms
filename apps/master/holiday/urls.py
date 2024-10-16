from django.urls import path
from .views import *
urlpatterns = [
    path('', HolidayListView.as_view(), name='holiday_list'),
    path('create/', HolidayCreateView.as_view(), name='holiday_create'),
    path('<int:pk>/update/', HolidayUpdateView.as_view(), name='holiday_update'),
    path('<int:pk>/delete/', HolidayDeleteView.as_view(), name='holiday_delete'),
]
