from django.urls import path
from .views import *
urlpatterns = [
    path('', PlanningActivityCategoryListView.as_view(), name='planning_activity_category_list'),
    path('create/', PlanningActivityCategoryCreateView.as_view(), name='planning_activity_category_create'),
    # path('<int:pk>/', PlanningActivityCategoryDetailView.as_view(), name='planning_activity_category_detail'),
    path('<int:pk>/update/', PlanningActivityCategoryUpdateView.as_view(), name='planning_activity_category_update'),
    path('<int:pk>/delete/', PlanningActivityCategoryDeleteView.as_view(), name='planning_activity_category_delete'),
]
