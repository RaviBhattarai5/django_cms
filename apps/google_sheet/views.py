from django.shortcuts import render
from utils.google_sheet import fetch_data_in_batches, fetch_sheet_data
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

def get_sheet_data(request):
    datas = []
    headers = []
    try:
        # datas = fetch_sheet_data()
        # headers = datas.pop(0)
        fetch_data_in_batches()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        messages.warning(request, e)
    return render(request, 'google_sheet/index.html', {
        'datas': datas,
        'headers': headers,
        'page_title': 'Google Sheet'
    })
    
    