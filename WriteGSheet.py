import os.path
from datetime import datetime, timedelta

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
#SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
#SAMPLE_SPREADSHEET_ID = "URs SAMPLE_SPREADSHEET_ID"
#SAMPLE_RANGE_NAME = "Sheet1!A3"

def ReadWriteSheet(Write, SCOPES, SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME, valueData):
  creds = None
  
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.


  NuovoToken=False
  if os.path.exists("token.json"):
    with open('TokenTime.txt', 'r') as file:
      old_date_str = file.read().strip()
      old_date = datetime.strptime(old_date_str, "%Y-%m-%d %H:%M:%S")

    if datetime.now() - old_date > timedelta(hours=24):
      NuovoToken=True
      with open("TokenTime.txt","w") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    else:
      creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid or NuovoToken==True:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
      creds = flow.run_local_server(port=3000)
      
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())


      

  try:
    service = build("sheets", "v4", credentials=creds)
    
    sheet = service.spreadsheets()

    if Write:
      result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME, valueInputOption="USER_ENTERED", body={"values":valueData}).execute()
      result={'values':valueData}

    else:
      result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=SAMPLE_RANGE_NAME).execute()

    return result
  
  except HttpError as err:
    return err

#print(ReadWriteSheet(False, SCOPES, SAMPLE_SPREADSHEET_ID, SAMPLE_RANGE_NAME, valueData))
