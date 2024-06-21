import os
import shutil
import subprocess
from PIL import Image

def compress_image(input_path, output_path, quality=20):
    try:
        img = Image.open(input_path)
        img.save(output_path, optimize=True, quality=quality)
        print(f"Compressed image: {output_path}")
    except Exception as e:
        print(f"Failed to compress image: {input_path}, Error: {e}")

def compress_video(input_path, output_path, crf=28):
    try:
        command = [
            'ffmpeg',
            '-i', input_path,
            '-c:v', 'libx264', '-crf', str(crf),
            '-c:a', 'aac', '-b:a', '128k',
            '-strict', 'experimental',
            output_path
        ]
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Compressed video: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to compress video: {input_path}, Error: {e}")

def compress_images_and_videos(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for root, dirs, files in os.walk(input_dir):
        for file in files:
            input_path = os.path.join(root, file)
            relative_path = os.path.relpath(input_path, input_dir)
            output_path = os.path.join(output_dir, relative_path)

            if not os.path.exists(os.path.dirname(output_path)):
                os.makedirs(os.path.dirname(output_path))

            if any(input_path.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png']):
                compress_image(input_path, output_path)

            elif any(input_path.lower().endswith(ext) for ext in ['.mp4', '.avi']):
                compress_video(input_path, output_path)

            else:
                shutil.copy(input_path, output_path)
                print(f"Copied file: {output_path}")

input_images_dir = "images"
output_compressed_dir = "compressed"

compress_images_and_videos(input_images_dir, output_compressed_dir)
