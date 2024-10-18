import os
import random
import time
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from googleapiclient.http import MediaFileUpload

class YouTubeUploader:
    
    def __init__(self, client_secret_file, api_service_name, api_version, scopes):
        # OAuth 2.0 credentials
        self.client_secret_file = client_secret_file
        self.api_service_name = api_service_name
        self.api_version = api_version
        self.scopes = scopes
        self.youtube = self.get_authenticated_service()

    def get_authenticated_service(self):
        # OAuth flow for authentication
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            self.client_secret_file, self.scopes)
        credentials = flow.run_local_server(port=0)
        youtube = googleapiclient.discovery.build(
            self.api_service_name, self.api_version, credentials=credentials)
        return youtube

    def upload_video(self, file, title="Test Title", description="Test Description", 
                    category="22", keywords="", privacy_status="public"):
        
        # Set tags if keywords are provided
        tags = keywords.split(",") if keywords else None
        
        # Create the video body with the metadata
        body = {
            "snippet": {
                "title": title,
                "description": description,
                "tags": tags,
                "categoryId": category
            },
            "status": {
                "privacyStatus": privacy_status
            }
        }
        
        # Prepare the media file for upload
        media_body = MediaFileUpload(file, chunksize=-1, resumable=True)
        
        # Insert request to upload the video
        insert_request = self.youtube.videos().insert(
            part="snippet,status",
            body=body,
            media_body=media_body
        )
        
        # Call the method to handle resumable upload
        self.resumable_upload(insert_request)
    
    def resumable_upload(self, insert_request):
        response = None
        error = None
        retry = 0
        
        while response is None:
            try:
                print("Uploading file...")
                status, response = insert_request.next_chunk()
                if response is not None:
                    if 'id' in response:
                        print(f"Video id '{response['id']}' was successfully uploaded.")
                    else:
                        raise Exception(f"Unexpected response: {response}")
            except googleapiclient.errors.HttpError as e:
                if e.resp.status in [500, 502, 503, 504]:
                    error = f"Retriable HTTP error {e.resp.status} occurred:\n{e.content}"
                else:
                    raise
            except (IOError, OSError) as e:
                error = f"Retriable error occurred: {e}"
            
            if error is not None:
                print(error)
                retry += 1
                if retry > 10:
                    raise Exception("No longer attempting to retry.")
                
                sleep_seconds = random.random() * (2 ** retry)
                print(f"Sleeping {sleep_seconds:.2f} seconds and retrying...")
                time.sleep(sleep_seconds)


