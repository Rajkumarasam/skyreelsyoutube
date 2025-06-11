# youtube_uploader.py

import os
import pickle
import google.auth.transport.requests
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


def get_authenticated_service():
    client_id = os.getenv("YOUTUBE_CLIENT_ID")
    client_secret = os.getenv("YOUTUBE_CLIENT_SECRET")
    refresh_token = os.getenv("YOUTUBE_REFRESH_TOKEN")

    if not all([client_id, client_secret, refresh_token]):
        raise EnvironmentError("Missing required YouTube credentials.")

    credentials = Credentials(
        token=None,
        refresh_token=refresh_token,
        token_uri="https://oauth2.googleapis.com/token", 
        client_id=client_id,
        client_secret=client_secret,
        scopes=["https://www.googleapis.com/auth/youtube.upload"] 
    )

    # Refresh the access token
    auth_request = google.auth.transport.requests.Request()
    credentials.refresh(auth_request)

    return build("youtube", "v3", credentials=credentials)


def upload_to_youtube(video_path, topic, script):
    print("📤 Starting YouTube upload...")

    youtube = get_authenticated_service()

    title = f"Top Health Benefits of {topic.title()} You Didn't Know!"
    description = f"Discover amazing benefits of {topic}!\n\nScript:\n{script[:500]}...\n\n#health #nutrition #{topic.replace(' ', '')}"
    tags = ["health", "wellness", topic, "nutrition", "daily tips"]

    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": "26"  # Health & Fitness
        },
        "status": {
            "privacyStatus": "public"
        }
    }

    insert_request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=MediaFileUpload(video_path)
    )

    response = insert_request.execute()
    video_id = response.get("id")
    print(f"✅ Upload successful! Video ID: {video_id}")
    print(f"🔗 https://youtu.be/{video_id}") 
