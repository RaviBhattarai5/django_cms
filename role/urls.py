from django.urls import path
from role import views
urlpatterns = [
    path('role/', views.role, name='role'),
    # path('role_list/', views.role_list, name='role_list')
]
