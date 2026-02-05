from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import base64
import os

load_dotenv()

app = Flask(__name__)
client = OpenAI()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    image_path = None

    if request.method == "POST":
        prompt = request.form["prompt"]

        try:
            # TEXT RESPONSE
            response = client.responses.create(
                model="gpt-4.1",
                input=prompt,
                temperature=1.2,
                max_output_tokens=100
            )
            result = response.output_text

            # IMAGE GENERATION
            img = client.images.generate(
                model="gpt-image-1",
                prompt=prompt,
                size="1024x1024"
            )

            image_bytes = base64.b64decode(img.data[0].b64_json)
            image_path = "static/output.png"

            with open(image_path, "wb") as f:
                f.write(image_bytes)

        except Exception as e:
            result = f"Error: {e}"

    return render_template("index.html", result=result, image=image_path)

if __name__ == "__main__":
    app.run(debug=True)
