from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

class GoogleDriveModule:
    def __init__(self, credentials_path):
        self.credentials = Credentials.from_authorized_user_file(credentials_path, ['https://www.googleapis.com/auth/drive'])
        self.service = build('drive', 'v3', credentials=self.credentials)