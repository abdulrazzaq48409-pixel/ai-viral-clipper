from flask import Flask, render_template, request
import os
import subprocess

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


@app.route("/", methods=["GET", "POST"])
def home():

    message = ""

    if request.method == "POST":

        video_url = request.form.get("video_url")

        if video_url:

            try:

                subprocess.run(
                    ["python", "main.py"],
                    input=video_url,
                    text=True,
                    cwd=BASE_DIR
                )

                message = "Viral clips generated successfully!"

            except Exception as e:
                message = f"Error: {e}"

    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)