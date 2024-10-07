from django.urls import path
from .views import *
urlpatterns = [
    path('', MasterActionTakenListView.as_view(), name='master_action_taken_list'),
    path('create/', MasterActionTakenCreateView.as_view(), name='master_action_taken_create'),
    # path('<int:pk>/', MasterActionTakenDetailView.as_view(), name='master_action_taken_detail'),
    path('<int:pk>/update/', MasterActionTakenUpdateView.as_view(), name='master_action_taken_update'),
    path('<int:pk>/delete/', MasterActionTakenDeleteView.as_view(), name='master_action_taken_delete'),
]
