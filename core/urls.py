from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('menus/', include('apps.menu.urls')),
    path('roles/', include('apps.roles.urls')),
    # path('', include('role.urls')),
] 
