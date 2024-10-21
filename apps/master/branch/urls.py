from django.urls import path
from .views import *
urlpatterns = [
    path('', BranchListView.as_view(), name='branch_list'),
    path('create/', BranchCreateView.as_view(), name='branch_create'),
    path('<int:pk>/', BranchDetailView.as_view(), name='branch_detail'),
    path('<int:pk>/update/', BranchUpdateView.as_view(), name='branch_update'),
    path('<int:pk>/delete/', BranchDeleteView.as_view(), name='branch_delete'),
]
