# voiceover_generator.py
import os
import edge_tts

async def run_tts(script, out_path):
    communicate = edge_tts.Communicate(script, \"en-IN-PrabhatNeural\")
    await communicate.save(out_path)

def generate_voiceover(script):
    import asyncio
    out_file = \"assets/audio/voiceover.mp3\"
    os.makedirs(\"assets/audio\", exist_ok=True)
    asyncio.run(run_tts(script, out_file))
    return out_file
