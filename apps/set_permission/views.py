from django.shortcuts import render
from .forms import SetPermissionForm
from apps.roles.models import Roles
from apps.menu.models import Menu
from apps.permission_type.models import PermissionType
from .models import SetPermission
from django.contrib import messages

def set_permission_view(request):
    selected_role = None
    if request.method == "POST":
        form = SetPermissionForm(request.POST)
        selected_role_id  = request.GET.get('role_id')
        SetPermission.objects.filter(role=selected_role_id ).delete()
        
        if selected_role_id:
            selected_role = Roles.objects.get(id=selected_role_id)
        if form.is_valid():
            for key, value in form.cleaned_data.items():
                if key.startswith(('role',)): # Skip non-checkbox fields
                    continue
                
                if value:
                    menu_id, permission_id = key.split('_')
                    
                    menu = Menu.objects.get(id=menu_id)
                    permission_type = PermissionType.objects.get(id=permission_id)
                    
                    SetPermission.objects.create(
                        menu=menu,
                        role=selected_role,
                        permission_type=permission_type
                    )
                    
            messages.success(request, 'Successfully assigned')
            
    else:
        if 'role_id' in request.GET and request.GET.get('role_id'):
            selected_role = Roles.objects.get(id=request.GET.get('role_id'))
            form = SetPermissionForm(role=selected_role) 
        else:
            form = SetPermissionForm()
    return render(request, 'set_permission/form.html', {
        'form': form,
        'fields': form.fields,
        'menus': Menu.objects.all(),
        'permission_types': PermissionType.objects.all(),
        'selected_role': selected_role
    })
