import os

def create_subtitle_file(result):

    os.makedirs("../subtitles", exist_ok=True)

    subtitle_path = "../subtitles/subtitles.srt"

    with open(
        subtitle_path,
        "w",
        encoding="utf-8"
    ) as file:

        for index, segment in enumerate(result["segments"], start=1):

            start = format_time(segment["start"])
            end = format_time(segment["end"])

            text = segment["text"]

            file.write(f"{index}\n")
            file.write(f"{start} --> {end}\n")
            file.write(f"{text}\n\n")

    return subtitle_path


def format_time(seconds):

    hours = int(seconds // 3600)

    minutes = int((seconds % 3600) // 60)

    secs = int(seconds % 60)

    milliseconds = int((seconds - int(seconds)) * 1000)

    return (
        f"{hours:02}:{minutes:02}:"
        f"{secs:02},{milliseconds:03}"
    )