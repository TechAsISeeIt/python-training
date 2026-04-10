from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=[{"role": "user", "content": user_input}]
    )

    print("Bot:", response.choices[0].message.content)
