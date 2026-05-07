import whisper

model = whisper.load_model("tiny")

def transcribe_audio(audio_path):

    result = model.transcribe(
        audio_path,
        language="ur"
    )

    with open(
        "../transcripts/transcript.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write("TRANSCRIPT:\n\n")

        for segment in result["segments"]:

            line = (
                f"[{segment['start']:.2f} - "
                f"{segment['end']:.2f}] "
                f"{segment['text']}\n"
            )

            file.write(line)

    print("Transcript saved successfully!")

    return result