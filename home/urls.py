from django.urls import path, include
from . import views
urlpatterns = [
    # path('', include("django.contrib.auth.urls")),
    path('', views.home, name='dashboard'),
    path('dashboard/', views.home, name='dashboard'),
    path('register/', views.register, name='register' ),
    path('login/', views.log_in, name='login' ),
    path('logout/', views.log_out, name='logout' ),
]
