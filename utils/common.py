from apps.master.pick_list.models import PickList


def arrange_pagination(context):
    paginator = context["paginator"]
    page_obj = context["page_obj"]
    current_page = page_obj.number
    total_pages = paginator.num_pages
    start_page = max(current_page - 1, 1)
    end_page = min(current_page + 1, total_pages)
    if current_page == 1:
        end_page = min(3, total_pages)
    elif current_page == total_pages:
        start_page = max(total_pages - 2, 1)
    context["page_range"] = range(start_page, end_page + 1)

    return context


def set_picklist_querysets(fields, fields_to_set):
    picklist_names = list(fields_to_set.values())
    parent_ids = PickList.objects.filter(pick_list_name__in=picklist_names).values(
        "pick_list_name", "id"
    )

    parent_id_map = {item["pick_list_name"]: item["id"] for item in parent_ids}
    for field_name, picklist_name in fields_to_set.items():
        parent_id = parent_id_map.get(picklist_name)
        fields[field_name].queryset = (
            PickList.objects.filter(parent_id=parent_id)
            if parent_id
            else PickList.objects.none()
        )
