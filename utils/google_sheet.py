from google.oauth2 import service_account
from googleapiclient.discovery import build

# def connect_sheet():
SERVICE_ACCOUNT_FILE = 'credentials/google_acc_key.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=credentials)
    
    # return service
    
# Accessing a specific spreadsheet
SPREADSHEET_ID = '1pmG--Geo0Uc5sPvJg7le8IsD4aLPbK3-gpEgJAzDBlw'
RANGE_NAME = 'intersted!A1:D10'

# Reading data
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
values = result.get('values', [])
print(values)

# Writing data (example)
# body = {
#     'values': [['Hello', 'World']]
# }

# sheet.values().append(spreadsheetId=SPREADSHEET_ID, range='Sheet1!A1', valueInputOption='RAW', body=body).execute()