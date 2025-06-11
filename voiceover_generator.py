voiceover_generator.py

import os import tempfile import subprocess

Check for Nari Labs Dia availability

USE_DIA = os.getenv("USE_DIA_TTS", "true").lower() in ("1","true","yes")

async def _edge_tts(script: str, out_path: str): import edge_tts communicate = edge_tts.Communicate(script, "en-US-AriaNeural") await communicate.save(out_path)

def generate_voiceover(script: str) -> str: """ Generate a voiceover MP3/WAV file for the given script. Uses Nari Labs Dia if available and configured, otherwise falls back to Edge-TTS. """ os.makedirs("assets/audio", exist_ok=True) out_wav = os.path.join("assets/audio", "voiceover_dia.wav")

if USE_DIA:
    try:
        # Use Nari Labs Dia via CLI
        # Assumes dia is installed: pip install git+https://github.com/nari-labs/dia.git
        result = subprocess.run(
            [
                "python", "-m", "dia.api.tts",
                "--model", "dia_hifi3_base",
                "--text", script,
                "--output", out_wav
            ],
            check=True
        )
        print(f"✅ Dia TTS generated: {out_wav}")
        return out_wav
    except Exception as e:
        print(f"⚠️ Dia TTS failed, falling back to Edge-TTS: {e}")

# Fallback to Edge-TTS
try:
    import asyncio
    out_mp3 = os.path.join("assets/audio", "voiceover_edge.mp3")
    asyncio.run(_edge_tts(script, out_mp3))
    print(f"✅ Edge-TTS generated: {out_mp3}")
    return out_mp3
except Exception as e:
    raise RuntimeError(f"Failed to generate voiceover: {e}")

