from google.oauth2 import service_account
from googleapiclient.discovery import build

SERVICE_ACCOUNT_FILE = 'credentials/google_acc_key.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1pmG--Geo0Uc5sPvJg7le8IsD4aLPbK3-gpEgJAzDBlw'
RANGE_NAME = 'intersted'

def connect_sheet():
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=credentials)
    return service


def fetch_sheet_data(spreadsheet_id=SPREADSHEET_ID, range_name=RANGE_NAME):
    service = connect_sheet()
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    return result.get('values', [])


def get_total_rows_from_metadata(spreadsheet_id=SPREADSHEET_ID, sheet_name=RANGE_NAME):
    service = connect_sheet()
    spreadsheet_metadata = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    sheet_metadata = next(sheet for sheet in spreadsheet_metadata['sheets'] if sheet['properties']['title'] == sheet_name)
    total_rows = sheet_metadata['properties']['gridProperties']['rowCount']
    return total_rows


def fetch_data_in_batches(spreadsheet_id=SPREADSHEET_ID, sheet_name=RANGE_NAME, start_row=1, batch_size=500, last_col='X'):
    service = connect_sheet()
    current_row = start_row
    total_rows = get_total_rows_from_metadata(spreadsheet_id, sheet_name)
    
    while current_row <= total_rows:
        end_row = min(current_row + batch_size - 1, total_rows)
        range_name = f"{sheet_name}!A{current_row}:{last_col}{end_row}"
        result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
        values = result.get('values', [])
        print(values)
        current_row += batch_size