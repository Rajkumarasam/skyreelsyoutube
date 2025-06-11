# youtube_uploader.py
import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


def upload_to_youtube(video_path, topic, script):
    youtube = build("youtube", "v3", developerKey=os.getenv("YOUTUBE_API_KEY"))

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
        "status": {"privacyStatus": "public"}
    }

    media = MediaFileUpload(video_path)
    youtube.videos().insert(part="snippet,status", body=body, media_body=media).execute()
