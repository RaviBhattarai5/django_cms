from django.urls import path
from .views import *
urlpatterns = [
    path('', StateListView.as_view(), name='state_list'),
    path('create/', StateCreateView.as_view(), name='state_create'),
    path('<int:pk>/', StateDetailView.as_view(), name='state_detail'),
    path('<int:pk>/update/', StateUpdateView.as_view(), name='state_update'),
    path('<int:pk>/delete/', StateDeleteView.as_view(), name='state_delete'),
]
