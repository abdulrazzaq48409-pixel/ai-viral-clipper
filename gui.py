import tkinter as tk
from tkinter import messagebox
import subprocess


def generate_clips():

    url = url_entry.get()

    if not url:
        messagebox.showerror(
            "Error",
            "Please paste a YouTube URL"
        )
        return

    status_label.config(
        text="Processing... Please wait"
    )

    root.update()

    process = subprocess.run(
        ["python", "main.py"],
        input=url,
        text=True,
        capture_output=True
    )

    if process.returncode == 0:

        status_label.config(
            text="Clips generated successfully!"
        )

        messagebox.showinfo(
            "Success",
            "AI clips generated!"
        )

    else:

        status_label.config(
            text="Error occurred"
        )

        messagebox.showerror(
            "Error",
            process.stderr
        )


# Main window
root = tk.Tk()

root.title("AI Viral Clipper")

root.geometry("500x300")


# Title
title_label = tk.Label(
    root,
    text="AI Viral Clipper",
    font=("Arial", 20)
)

title_label.pack(pady=20)


# URL input
url_entry = tk.Entry(
    root,
    width=50
)

url_entry.pack(pady=10)


# Generate button
generate_button = tk.Button(
    root,
    text="Generate Viral Clips",
    command=generate_clips,
    height=2,
    width=25
)

generate_button.pack(pady=20)


# Status
status_label = tk.Label(
    root,
    text="Waiting..."
)

status_label.pack(pady=10)


root.mainloop()