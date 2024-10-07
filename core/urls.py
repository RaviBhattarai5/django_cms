from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('menus/', include('apps.administrator.menu.urls')),
    path('roles/', include('apps.administrator.roles.urls')),
    path('permission_type/', include('apps.administrator.permission_type.urls')),
    path('users/', include('apps.administrator.users.urls')),
    path('set-permission/', include('apps.administrator.set_permission.urls')),

    path('master-action-taken/', include('apps.master.master_action_taken.urls')),
    path('department/', include('apps.master.department.urls')),
    path('enquiry-state/', include('apps.master.enquiry_state.urls')),
    path('observed-problem/', include('apps.master.observed_problem.urls')),
    path('operation-performed/', include('apps.master.operation_performed.urls')),
    path('planning-activity-category/', include('apps.master.planning_activity_category.urls')),
    # path('', include('role.urls')),
] 
