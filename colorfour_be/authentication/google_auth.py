import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/calendar"]

def get_google_credentials():
  creds = None
  credentials_path = os.getenv('GOOGLE_CREDENTIALS_PATH', 'credentials.json')
  token_path = os.getenv('GOOGLE_TOKEN_PATH', 'token.json')

  if os.path.exists(token_path):
    creds = Credentials.from_authorized_user_file(token_path, SCOPES)
  
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
      creds = flow.run_local_server(port=0)
    with open(token_path, "w") as token:
      token.write(creds.to_json())
  
  return creds
