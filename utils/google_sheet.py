from google.oauth2 import service_account
from googleapiclient.discovery import build

SPREADSHEET_ID = '1pmG--Geo0Uc5sPvJg7le8IsD4aLPbK3-gpEgJAzDBlw'
SERVICE_ACCOUNT_FILE = 'credentials/google_acc_key.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def connect_sheet():
    RANGE_NAME = 'intersted!A:I'
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=credentials)
    
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
    return result.get('values', [])