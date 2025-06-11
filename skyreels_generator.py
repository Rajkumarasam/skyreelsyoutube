# skyreels_generator.py
import os
import torch
from diffusers import DiffusionPipeline

class SkyReelsGenerator:
    def __init__(self, model_name="SkyworkAI/skyreels-v2-540p", device=None):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        print(f"🚀 Loading SkyReels-V2 model on {self.device}...")
        self.pipeline = DiffusionPipeline.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            variant="fp16"
        ).to(self.device)

    def generate_video(self, prompt: str, num_frames: int = 60, fps: int = 24):
        print(f"🎬 Generating video for prompt: \"{prompt}\"")
        out = self.pipeline(
            prompt=prompt,
            num_inference_steps=50,
            num_frames=num_frames,
            guidance_scale=7.5,
            height=540,
            width=960,
        ).videos[0]

        os.makedirs("assets/videos", exist_ok=True)
        safe_prompt = "".join(c if c.isalnum() else "_" for c in prompt[:30])
        out_path = f"assets/videos/skyreel_{safe_prompt}.mp4"

        out.save(out_path, fps=fps)
        print(f"✅ Saved video: {out_path}")
        return out_path
