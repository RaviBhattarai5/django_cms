from django.urls import path
from .views import *
urlpatterns = [
    path('', PlanningActivityListView.as_view(), name='planning_activity_list'),
    path('create/', PlanningActivityCreateView.as_view(), name='planning_activity_create'),
    # path('<int:pk>/', PlanningActivityDetailView.as_view(), name='planning_activity_detail'),
    path('<int:pk>/update/', PlanningActivityUpdateView.as_view(), name='planning_activity_update'),
    path('<int:pk>/delete/', PlanningActivityDeleteView.as_view(), name='planning_activity_delete'),
]
