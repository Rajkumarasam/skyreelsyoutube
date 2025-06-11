import os
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip


def generate_images_and_video(prompts, voice_path, output_video="assets/final/final_video.mp4"):
    os.makedirs("assets/images", exist_ok=True)
    os.makedirs("assets/final", exist_ok=True)

    clips = []
    for idx, prompt in enumerate(prompts):
        img_path = f"assets/images/fallback_{idx+1}.jpg"
        with open(img_path, "wb") as f:
            f.write(b"\x00")
        clip = ImageClip(img_path).set_duration(5).resize(height=2160)
        clips.append(clip)

    final_clip = concatenate_videoclips(clips, method="compose")
    audio = AudioFileClip(voice_path)
    final_video = final_clip.set_audio(audio)

    final_video.write_videofile(output_video, fps=30, codec='libx264')
    return output_video
