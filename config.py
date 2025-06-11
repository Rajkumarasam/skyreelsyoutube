#config.py
import os
from dotenv import load_dotenv

load_dotenv()

# API Keys (will be set as GitHub secrets)
YOUTUBE_API_KEY = os.getenv('AIzaSyAfOgTlNHPBhAfBeTbDiVUE8iTIk0OT-Rk')
YOUTUBE_CLIENT_ID = os.getenv('867486016625-itl6fcouu5elmfd3sv3esq0ovovhpsao.apps.googleusercontent.com')
YOUTUBE_CLIENT_SECRET = os.getenv('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')
YOUTUBE_REFRESH_TOKEN = os.getenv('1//0gKMTG6so1kGPCgYIARAAGBASNwF-L9IrCKZXT2MUffv9NvqtngcX-LZTKJ_-hVIvY778rFyRdCFNjL78dZZPd5umNOPFB1trY5U')
GROQ_API_KEY = os.getenv('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')
BING_COOKIE = os.getenv('1tI0jaC3B4pAGBVyBlQHW6hc7qziYRChM-LnTC4MTXLbOjek1_omleVyDnQUpZ3IxZyG-45noPZIcvJJvxldDD4SzzTWJkjrLwxI4TBbqJwLBE1CeZ9N-kvvcv7qKYZZ70TlDpibtuCH7zb4VJKm3-JoQD3G7q8ZNHV3zw7_LioPX6OGEAN_NhKj0I5nBdNLvx64Z6AjbMmm-GrTjq1PkmENFJSL4HJxkct97JVrv_jM')

# Channel Configuration
CHANNEL_ID = "@PeopleSane"  # You'll update this
CHANNEL_NAME = "People Sane"  # Update this

# Video Configuration
VIDEO_LENGTH = 180  # 3 minutes in seconds
VIDEO_RESOLUTION = "3840x2160"  # 4K
DAILY_UPLOAD_TIME = "03:30"  # 9:00 AM IST in UTC

# Content Configuration
HEALTH_TOPICS_FILE = "assets/health_topics.json"
BACKGROUND_MUSIC_DIR = "assets/music/"
FONTS_DIR = "assets/fonts/"

# Image Style
IMAGE_STYLE = "scroll painting of chrysanthemums in background, ink wash style --v 7q, traditional Chinese art, watercolor, serene"

# Video Templates
INTRO_TEXT = "Welcome to your daily health tip!"
OUTRO_TEXT = "Subscribe for more health secrets!"
CALL_TO_ACTION = "What's your experience with {topic}? Comment below!"
