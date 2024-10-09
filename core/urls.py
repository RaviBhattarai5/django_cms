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
    path('master-country/', include('apps.master.country.urls')),
    path('master-state/', include('apps.master.state.urls')),
    path('master-branch/', include('apps.master.branch.urls')),
    path('master-product-bin/', include('apps.master.product_bin.urls')),
    path('master-product-category/', include('apps.master.product_category.urls')),
    path('master-products/', include('apps.master.products.urls')),
    path('master-group/', include('apps.master.group.urls')),
    path('master-serial-status/', include('apps.master.serial_status.urls')),

] 
