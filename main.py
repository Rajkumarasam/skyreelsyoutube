# main.py
import os
from content_generator import generate_script_and_prompts
from voiceover_generator import generate_voiceover
from image_to_video import generate_images_and_video
from youtube_uploader import upload_to_youtube


def main():
    print("\n🚀 Starting Automated Health Video Creation")

    topic = get_daily_topic()
    print(f"\n📝 Topic: {topic}")

    script, prompts = generate_script_and_prompts(topic)
    print(f"\n✅ Script Generated\n")

    voice_path = generate_voiceover(script)
    print(f"\n✅ Voiceover Created: {voice_path}")

    video_path = generate_images_and_video(prompts, voice_path)
    print(f"\n✅ Final Video Created: {video_path}")

    upload_to_youtube(video_path, topic, script)
    print("\n📤 Uploaded to YouTube Successfully!")


def get_daily_topic():
    topics = [
        "blueberries", "spinach", "almonds", "turmeric", "avocado", "kale",
        "carrots", "ginger", "chia seeds", "green tea"
    ]
    from datetime import datetime
    day_index = datetime.now().timetuple().tm_yday % len(topics)
    return topics[day_index]


if __name__ == "__main__":
    main()
