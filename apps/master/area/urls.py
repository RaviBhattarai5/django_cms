from django.urls import path
from .views import *

urlpatterns = [
    path("", AreaListView.as_view(), name="area_list"),
    path("create/", AreaCreateView.as_view(), name="area_create"),
    # path('<int:pk>/', AreaDetailView.as_view(), name='area_detail'),
    path("<int:pk>/update/", AreaUpdateView.as_view(), name="area_update"),
    path("<int:pk>/delete/", AreaDeleteView.as_view(), name="area_delete"),
]
