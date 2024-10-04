from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('menus/', include('apps.menu.urls')),
    path('roles/', include('apps.roles.urls')),
    path('permission_type/', include('apps.permission_type.urls')),
    path('users/', include('apps.users.urls')),
    path('set-permission/', include('apps.set_permission.urls')),
    path('master-action-taken/', include('apps.master.master_action_taken.urls')),
    # path('', include('role.urls')),
] 
