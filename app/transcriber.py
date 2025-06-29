from openai import OpenAI

client = OpenAI()

def transcribe_audio(file_path):
    with open(file_path, "rb") as f:
        transcript = client.audio.transcriptions.create(
            file=f,
            model="whisper-1"
        )
    return transcript.text

