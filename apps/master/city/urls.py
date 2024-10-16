from django.urls import path
from .views import *

urlpatterns = [
    path("", CityListView.as_view(), name="city_list"),
    path("create/", CityCreateView.as_view(), name="city_create"),
    # path('<int:pk>/', CityDetailView.as_view(), name='city_detail'),
    path("<int:pk>/update/", CityUpdateView.as_view(), name="master_city_update"),
    path("<int:pk>/delete/", CityDeleteView.as_view(), name="master_city_delete"),
]
