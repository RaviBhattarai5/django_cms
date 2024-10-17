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
    path('planning-activity/', include('apps.master.planning_activity.urls')),
    path('master-country/', include('apps.master.country.urls')),
    path('master-state/', include('apps.master.state.urls')),
    path('master-branch/', include('apps.master.branch.urls')),
    path('master-product-bin/', include('apps.master.product_bin.urls')),
    path('master-product-category/', include('apps.master.product_category.urls')),
    # path('master-product-group/', include('apps.master.product_group.urls')),
    # path('master-product/', include('apps.master.product.urls')),
    path('city/', include('apps.master.city.urls')),
    path('master-products/', include('apps.master.products.urls')),
    path('master-group/', include('apps.master.group.urls')),
    path('master-serial-status/', include('apps.master.serial_status.urls')),
    path('master-pick-list/', include('apps.master.pick_list.urls')),
    path('master-customer/', include('apps.master.customer.urls')),
    path('master-holiday/', include('apps.master.holiday.urls')),
    path('master-holiday-in-area/', include('apps.master.holiday_in_area.urls')),
    path('master-holiday-Type/', include('apps.master.holiday_type.urls')),
    path('area/',include('apps.master.area.urls')),
<<<<<<< HEAD
    path('ecc/',include('apps.master.ecc.urls')),
    path('transporter/',include('apps.master.transporter.urls')),
=======
    path('party/',include('apps.master.party.urls')),
>>>>>>> 928ae2adb95d1761e266b2e69198031eee13c3f0
] 
