from moviepy.editor import VideoFileClip, AudioFileClip

    def add_audio_to_video(self, video_path, audio_path):
        print("🔊 Adding voiceover to video...")
        v = VideoFileClip(video_path)
        a = AudioFileClip(audio_path)
        final = v.set_audio(a).set_duration(v.duration)
        out = video_path.replace(".mp4", "_with_audio.mp4")
        final.write_videofile(out, codec="libx264", audio_codec="aac")
        return out
