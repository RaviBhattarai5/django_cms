from background_task import background
from utils.google_sheet import connect_sheet, get_total_rows_from_metadata
from utils.common import init_process_tracking, arrange_date_time_formate, arrange_date
from apps.google_sheet.models import InterestedSheet
import logging

logger = logging.getLogger(__name__)
spreadsheet_id='1pmG--Geo0Uc5sPvJg7le8IsD4aLPbK3-gpEgJAzDBlw'
sheet_name = 'intersted'
start_row = 1
batch_size = 500
last_col = 'U'

def store_data(data):
    if not data[1]:
        return
    
    InterestedSheet.objects.create(
        init_date = arrange_date_time_formate(data[1]),
        ph_no = data[2],
        msg = data[3],
        interest = data[4],
        alt_num = data[5],
        state = data[6],
        source = data[7],
        assign_to = data[8],
        follow_up = data[9],
        status = data[10],
        remarks1 = data[11],
        remarks2 = data[12],
        remarks3 = data[13],
        enquiry_no = data[14],
        enquiry_date = arrange_date(data[15]),
        enquiry_caller_name = data[16],
        calling_status = data[17],
        is_in_qualified_lead = data[18],
        first_source = data[19],
        fb_lead_no = data[20]
    )

def fetch_and_store_in_batch(current_row, total_rows, service, progress):
    while current_row <= total_rows:
        end_row = min(current_row + batch_size - 1, total_rows)
        range_name = f"{sheet_name}!A{current_row}:{last_col}{end_row}"
        result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
        values = result.get('values', [])
        
        if values:
            InterestedSheet.objects.all().delete()
            for row in values:
                    store_data(row)
        progress.processed_rows = min(current_row + batch_size - 1, total_rows)
        progress.save()            
        current_row += batch_size

@background(schedule=0)
def fetch_and_store_data_task(spreadsheet_id=spreadsheet_id, sheet_name=sheet_name):
    try:
        service = connect_sheet()
        current_row = start_row
        total_rows = get_total_rows_from_metadata(spreadsheet_id, sheet_name)
        progress = init_process_tracking(sheet_name, total_rows)
        fetch_and_store_in_batch(current_row, total_rows, service, progress)
        progress.status = 'completed'
        progress.save()
        
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        progress.status = 'failed'
        progress.error_message = str(e)
        progress.save()
        