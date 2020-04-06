# learn about how to work with gspread at https://gspread.readthedocs.io/en/latest/user-guide.html#opening-a-spreadsheet

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("INTERNAL_Coffee - a hug in a mug - data sheet")

# The worksheet 'General Info' is being selected with under the variable 'GeneralInfo' and can now be worked with
# like selecting a cell etc.
GeneralInfo = sheet.worksheet("General Info")
