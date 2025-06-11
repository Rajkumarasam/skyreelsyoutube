import os
import asyncio
import edge_tts


async def _edge_tts(script: str, out_path: str):
    communicate = edge_tts.Communicate(script, voice="en-US-AriaNeural")
    await communicate.save(out_path)


def generate_voiceover(script: str, filename="assets/audio/voiceover.mp3"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    try:
        asyncio.run(_edge_tts(script, filename))
        print(f"✅ Voiceover saved as {filename}")
        return filename
    except Exception as e:
        print(f"❌ Failed to generate voiceover: {e}")
        return None
