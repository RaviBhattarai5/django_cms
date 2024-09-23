from django.urls import path
from apps.roles import views
urlpatterns = [
    path('', views.RolesView.as_view(), name='roles'),
    path('edit/<int:pk>/', views.RolesUpdateView.as_view(), name="edit"),
    path('delete/<int:pk>/', views.RolesDeleteView.as_view(), name="delete"),
]
