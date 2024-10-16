from django.views.generic import ListView
from .models import InterestedSheet
from utils.common import arrange_pagination
from django.shortcuts import render
from utils.google_sheet import fetch_data_in_batches, fetch_sheet_data
from background_tasks.interested_sheet_task import fetch_and_store_data_task
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

# def get_sheet_data(request):
#     datas = []
#     headers = []
#     try:
#         # datas = fetch_sheet_data()
#         # headers = datas.pop(0)
#         fetch_data_in_batches()
#     except Exception as e:
#         logger.error(f"An error occurred: {e}")
#         messages.warning(request, e)
#     return render(request, 'google_sheet/index.html', {
#         'datas': datas,
#         'headers': headers,
#         'page_title': 'Google Sheet'
#     })
    
def get_sheet_data(request):
    datas = []
    headers = []
    try:
        fetch_and_store_data_task()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        messages.warning(request, e)
    return render(request, 'google_sheet/index.html', {
        'datas': datas,
        'headers': headers,
        'page_title': 'Google Sheet'
    })

class InterestedSheetListView(ListView):
    model = InterestedSheet
    template_name = 'google_sheet/index.html'
    context_object_name = 'datas'
    paginate_by = 100
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Menu'
        context['breadcrumbs'] = [{'name':'Dashboard', 'url':'dashboard'},{'name':'Google Sheet', 'url':'menu_list'}]
        
        context = arrange_pagination(context)
        return context