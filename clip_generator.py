import subprocess
import os
import re

from title_generator import generate_title


def clean_filename(text):

    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)

    text = text.replace(" ", "_")

    return text[:40]


def generate_clips(viral_clips):

    os.makedirs("../clips/generated", exist_ok=True)

    if len(viral_clips) == 0:
        print("No viral clips detected!")
        return

    for index, clip in enumerate(viral_clips):

        start = clip["start"]
        end = clip["end"]

        duration = end - start

        title = generate_title(clip["text"])

        clean_title = clean_filename(title)

        output_file = (
            f"../clips/generated/"
            f"{index+1}_{clean_title}.mp4"
        )

        subtitle_style = (
            "Fontsize=18,"
            "PrimaryColour=&Hffffff&,"
            "OutlineColour=&H000000&,"
            "BorderStyle=1,"
            "Outline=2,"
            "Shadow=1,"
            "Alignment=2,"
            "MarginV=40"
        )

        command = [
            "ffmpeg",
            "-y",

            "-ss",
            str(start),

            "-i",
            "../videos/test_video.mp4",

            "-t",
            str(duration),

            "-vf",
            (
                "crop=ih*9/16:ih,"
                f"subtitles=../subtitles/subtitles.srt:"
                f"force_style='{subtitle_style}'"
            ),

            "-c:v",
            "libx264",

            "-c:a",
            "aac",

            output_file
        ]

        print(f"Creating clip {index+1}...")

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print(f"SUCCESS: {output_file}")
        else:
            print("ERROR:")
            print(result.stderr)