# utils.py
from django.core.paginator import Paginator

def get_paginated_queryset(queryset, request, per_page):
    paginator = Paginator(queryset, per_page)  # Show `per_page` items per page
    page_number = request.GET.get('page')  # Get the page number from the request
    page_obj = paginator.get_page(page_number)  # Get the page of jobs

    # Create dynamic range for pagination 
    current_page = page_obj.number
    total_pages = paginator.num_pages
    page_range = list(paginator.page_range)

    # Adjust the range of pages to display dynamically around the current page
    start_index = max(current_page - 3, 0)
    end_index = min(current_page + 2, total_pages)
    page_range = page_range[start_index:end_index]

    return page_obj, page_range
