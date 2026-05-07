import yt_dlp
import subprocess

from transcriber import transcribe_audio
from subtitle_generator import create_subtitle_file
from viral_detector import detect_viral_segments
from clip_generator import generate_clips
from title_generator import generate_title

url = input("Paste YouTube URL: ")

# Download full video
ydl_opts = {
    'format': 'mp4',
    'outtmpl': '../videos/video.mp4'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Video downloaded successfully!")

# Create short test video (first 2 minutes only)
trim_command = [
    "ffmpeg",
    "-y",
    "-i",
    "../videos/video.mp4",
    "-t",
    "120",
    "../videos/test_video.mp4"
]

subprocess.run(trim_command)

print("Test video created!")

# Extract audio from test video
command = [
    "ffmpeg",
    "-y",
    "-i",
    "../videos/test_video.mp4",
    "../audio/audio.mp3"
]

subprocess.run(command)

print("Audio extracted successfully!")

# AI transcription
result = transcribe_audio("../audio/audio.mp3")

# Create subtitle file
subtitle_file = create_subtitle_file(result)

print("Subtitle file created!")

# Detect viral moments
viral_clips = detect_viral_segments(result)

# Save viral clips with AI titles
with open(
    "../clips/viral_clips.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write("VIRAL CLIPS FOUND:\n\n")

    for clip in viral_clips:

        title = generate_title(clip["text"])

        line = (
            f"TITLE: {title}\n"
            f"SCORE: {clip['score']}\n"
            f"TIME: [{clip['start']:.2f} - "
            f"{clip['end']:.2f}]\n"
            f"TEXT: {clip['text']}\n\n"
        )

        file.write(line)

print("Viral clips saved successfully!")

# Generate actual video clips
generate_clips(viral_clips)

print("All clips generated successfully!")