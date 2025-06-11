# image_to_video.py
import os
from moviepy.editor import *


def generate_images_and_video(prompts, voice_path):
    os.makedirs("assets/images", exist_ok=True)
    os.makedirs("assets/final", exist_ok=True)

    clips = []
    for idx, prompt in enumerate(prompts):
        # Use SkyReels CLI or placeholder fallback image
        img_path = f"assets/images/fallback_{idx+1}.jpg"
        with open(img_path, "wb") as f:
            f.write(b"\x00")  # dummy placeholder
        clip = ImageClip(img_path).set_duration(5).resize(height=2160)
        clips.append(clip)

    final_clip = concatenate_videoclips(clips, method="compose")
    audio = AudioFileClip(voice_path)
    final_video = final_clip.set_audio(audio)

    out_path = "assets/final/final_video.mp4"
    final_video.write_videofile(out_path, fps=30, codec='libx264')
    return out_path
