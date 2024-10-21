from django.urls import path
from .views import *
urlpatterns = [
    path('', PickListView.as_view(), name='pick_list'),
    path('create/', PickListCreateView.as_view(), name='pick_list_create'),
    path('<int:pk>/', PickListDetailView.as_view(), name='pick_list_detail'),
    path('<int:pk>/update/', PickListUpdateView.as_view(), name='pick_list_update'),
    path('<int:pk>/delete/', PickListDeleteView.as_view(), name='pick_list_delete'),
]
