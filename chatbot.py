import os
from dotenv import load_dotenv
import openai

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = os.environ[OPENAI_API_KEY]

print("Works!")


def chat_with_gpt(prompt, MaxToken=50, outputs=3):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}],
        max_tokens=MaxToken,
        n = outputs,
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
    
        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)
