from apps.administrator.menu.models import Menu
from apps.administrator.users.models import UserRole
from apps.administrator.permission_type.models import PermissionType

def menu_context(request):
    if not request.user.is_authenticated:
        return {'menu_hierarchy': []}
    
    user = request.user

    if user.is_superuser:
        top_level_menus = Menu.objects.filter(parent__isnull=True).prefetch_related('children')
    else:
        user_roles = UserRole.objects.filter(user=user).values_list('role_id', flat=True)
        browse_permission = PermissionType.objects.get(name='Browse')
        
        top_level_menus = Menu.objects.filter(
            parent__isnull=True,
            setpermission__role_id__in=user_roles,
            setpermission__permission_type=browse_permission
        ).distinct().prefetch_related('children')

    menu_hierarchy = [
        {
            'menu': menu,
            'children': get_children(menu, user, user_roles if not user.is_superuser else None, browse_permission if not user.is_superuser else None)
        }
        for menu in top_level_menus
    ]
    
    return {'menu_hierarchy': menu_hierarchy}


def get_children(menu, user, user_roles=None, browse_permission=None):
    if user.is_superuser:
        children = menu.children.all()
    else:
        children = menu.children.filter(
            setpermission__role_id__in=user_roles,
            setpermission__permission_type=browse_permission
        ).distinct()

    return [
        {
            'menu': child,
            'children': get_children(child, user, user_roles, browse_permission)
        }
        for child in children
    ]
