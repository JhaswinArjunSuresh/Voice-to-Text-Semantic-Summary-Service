# 🎤 Voice-to-Text + Semantic Summary Service

This Flask app transcribes audio using Whisper and summarizes it with GPT.

## Usage
- `POST /transcribe` with `multipart/form-data` containing an audio file.
- `POST /summary` with JSON `{ "text": "..." }`.

## Run locally
```bash
pip install -r requirements.txt
export OPENAI_API_KEY=your_key_here
python app/main.py

