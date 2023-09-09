import os
import subprocess
import argparse

def create_video_from_images(input_folder, output_file, framerate=24):
    if not os.path.exists(input_folder):
        raise ValueError("Input folder does not exist")

    image_files = sorted([f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])

    if not image_files:
        raise ValueError("No image files found in the input folder")

    command = [
        "ffmpeg",
        "-framerate", str(framerate),
        "-i", os.path.join(input_folder, "%d.jpg"),  # Adjust the format based on your image filenames
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-crf", "18",
        "-r", str(framerate),
        "-y", output_file
    ]

    subprocess.run(command)

def main():
    parser = argparse.ArgumentParser(description="Convert images to a video using ffmpeg")
    parser.add_argument("input_folder", help="Path to the folder containing input images")
    parser.add_argument("output_file", help="Output video file name")
    parser.add_argument("--framerate", type=int, default=24, help="Output video framerate")
    args = parser.parse_args()

    create_video_from_images(args.input_folder, args.output_file, args.framerate)

if __name__ == "__main__":
    main()
