from apps.menu.models import Menu

def menu_context(request):
    top_level_menus = Menu.objects.filter(parent__isnull=True)
    menu_hierarchy = []

    for menu in top_level_menus:
        menu_hierarchy.append({
            'menu': menu,
            'children': get_children(menu)
        })
    return {'menu_hierarchy': menu_hierarchy}

def get_children(menu):
    children = menu.children.all()
    children_hierarchy = []

    for child in children:
        children_hierarchy.append({
            'menu': child,
            'children': get_children(child)
        })

    return children_hierarchy