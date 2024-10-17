from django.urls import path
from .views import *
urlpatterns = [
    path('', ECCListView.as_view(), name='ecc_list'),
    path('create/', ECCCreateView.as_view(), name='ecc_create'),
    # path('<int:pk>/', DepartmentDetailView.as_view(), name='department_detail'),
    path('<int:pk>/update/',ECCUpdateView.as_view(), name='ecc_update'),
    path('<int:pk>/delete/', ECCDeleteView.as_view(), name='ecc_delete'),
]
