from openai import OpenAI
client = OpenAI()

def summarize_text(text):
    prompt = f"Summarize this text in a concise way:\n\n{text}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

