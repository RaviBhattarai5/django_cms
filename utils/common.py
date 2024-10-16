from datetime import datetime
from apps.google_sheet.models import DataFetchProgress

def arrange_pagination(context):
    paginator = context['paginator']
    page_obj = context['page_obj']
    current_page = page_obj.number
    total_pages = paginator.num_pages
    start_page = max(current_page - 1, 1)
    end_page = min(current_page + 1, total_pages)
    if current_page == 1:
        end_page = min(3, total_pages)
    elif current_page == total_pages:
        start_page = max(total_pages - 2, 1)
    context['page_range'] = range(start_page, end_page + 1)
    
    return context

def arrange_date_time_formate(date_str):
    try:
        if "/" in date_str:
            dt = datetime.strptime(date_str, "%m/%d/%Y %H:%M")
        elif "-" in date_str:
            dt = datetime.strptime(date_str, "%d-%m-%Y %H:%M")
        return dt
    except ValueError as e:
        print(f"Error parsing date: {e}")
        return None
    
def arrange_date(date_str):
    try:
        date = arrange_date_time_formate(date_str).date()
        return date
    except ValueError as e:
        print(f"Error parsing date: {e}")
        return None

def init_process_tracking(sheet_name, total_rows):
    progress, created = DataFetchProgress.objects.get_or_create(task_id=sheet_name)
    progress.total_rows = total_rows
    progress.status = 'in_progress'
    progress.save()
    return progress