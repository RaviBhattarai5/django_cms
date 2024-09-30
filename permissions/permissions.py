from django.core.cache import cache
from django.contrib.auth.models import User
from collections import defaultdict
from apps.set_permission.models import SetPermission
from apps.users.models import UserRole

def has_permission(user: User, menu, permission_type):
    cache_key = 'role_menu_permissions'
    role_permissions = cache.get(cache_key)
    roles = UserRole.objects.filter(user_id=user.id).values_list('role_id', flat=True)
    
    if user.is_superuser:
        return True
    
    if role_permissions is None:
        role_permissions = defaultdict(lambda: defaultdict(list))
        permissions = SetPermission.objects.select_related('role', 'menu', 'permission_type').all()
        
        for permission in permissions:
            role_name = permission.role.role_name
            menu_name = permission.menu.slug
            permission_type_name = permission.permission_type.name
            
            role_permissions[role_name][menu_name].append(permission_type_name)
            
            cache.set(cache_key, dict(role_permissions), timeout=60 * 60 * 24)
        print(role_permissions)
    
    for role in roles:
        if permission_type in role_permissions[role][menu]:
            return True
    
    return False