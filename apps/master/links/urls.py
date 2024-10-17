from django.urls import path
from .views import *

urlpatterns = [
    path('',LinkListView.as_view(), name='link_list'),
    path('create/', LinkCreateView.as_view(), name='link_create'),
    # path('<int:pk>/', LinkDetailView.as_view(), name='link_detail'),
    path('<int:pk>/update/', LinkUpdateView.as_view(), name='link_update'),
    path('<int:pk>/delete/', LinkDeleteView.as_view(), name='link_delete'),
]