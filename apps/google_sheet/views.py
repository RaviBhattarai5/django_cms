from django.shortcuts import render
from utils.google_sheet import connect_sheet
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)

def get_sheet_data(request):
    datas = []
    headers = []
    try:
        datas = connect_sheet()
        headers = datas.pop(0)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        messages.warning(request, e)
    return render(request, 'google_sheet/index.html', {
        'datas': datas,
        'headers': headers,
        'page_title': 'Google Sheet'
    })
    
    