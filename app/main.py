from flask import Flask, request, jsonify
import os, uuid
from .transcriber import transcribe_audio
from .summarizer import summarize_text

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files["file"]
    filename = f"{uuid.uuid4()}_{file.filename}"
    path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(path)
    text = transcribe_audio(path)
    return jsonify({"transcript": text})

@app.route("/summary", methods=["POST"])
def summary():
    data = request.get_json()
    text = data.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    summary = summarize_text(text)
    return jsonify({"summary": summary})

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

