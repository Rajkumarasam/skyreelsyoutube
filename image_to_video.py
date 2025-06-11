# image_to_video.py
from skyreels_generator import SkyReelsGenerator


def generate_images_and_video(prompts, voice_path):
    """
    Uses SkyReels-V2 to generate a video from text prompts.
    Then combines it with voiceover.
    """
    print("🎥 Generating video with SkyReels-V2...")

    generator = SkyReelsGenerator()
    video_path = generator.generate_video(prompts[0])  # Use first prompt for now

    print("🔊 Adding voiceover to video...")
    final_video_path = add_audio_to_video(video_path, voice_path)

    return final_video_path


def add_audio_to_video(video_path, audio_path):
    from moviepy.editor import VideoFileClip, AudioFileClip
    print("🔊 Syncing voiceover with video...")
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)

    # Match durations
    audio = audio.set_duration(video.duration)
    final_video = video.set_audio(audio)

    output_path = video_path.replace(".mp4", "_with_audio.mp4")
    final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")
    print(f"✅ Final video saved at: {output_path}")

    return output_path
