import os
from skyreels_generator import SkyReelsGenerator

def main():
    os.makedirs("assets/videos", exist_ok=True)
    gen = SkyReelsGenerator()
    video = gen.generate_video("A serene health tip explanation in documentary style", num_frames=120)
    print("Video generated:", video)

if __name__ == "__main__":
    main()
