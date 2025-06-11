# voiceover_generator.py

import os
import subprocess
import asyncio
import edge_tts


def generate_voiceover(script: str, filename="assets/audio/voiceover.mp3"):
    """
    Generate a voiceover using Nari Labs Dia first, fall back to Edge-TTS if it fails.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    USE_DIA = os.getenv("USE_DIA_TTS", "true").lower() in ("1", "true", "yes")

    # Try Dia first
    if USE_DIA:
        try:
            print("🔊 Using Nari Labs Dia for TTS...")
            result = subprocess.run(
                [
                    "python", "-m", "dia.api.tts",
                    "--model", "dia_hifi3_base",
                    "--text", script,
                    "--output", filename
                ],
                check=True,
                capture_output=True,
                text=True
            )
            print(f"✅ Dia TTS generated: {filename}")
            return filename
        except Exception as e:
            print(f"⚠️ Dia TTS failed, falling back to Edge-TTS: {e}")

    # Fallback to Edge-TTS
    try:
        print("🔊 Falling back to Edge-TTS...")
        asyncio.run(_edge_tts(script, filename))
        print(f"✅ Edge-TTS generated: {filename}")
        return filename
    except Exception as e:
        raise RuntimeError(f"❌ Failed to generate voiceover: {e}")


async def _edge_tts(script: str, out_path: str):
    communicate = edge_tts.Communicate(script, voice="en-US-AriaNeural")
    await communicate.save(out_path)
