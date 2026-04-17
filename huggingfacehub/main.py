from functools import lru_cache
import os
import sys
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(
    api_key=os.environ["HUGGINGFACEHUB_API_TOKEN"],
)
print("Client created successfully")

@lru_cache(maxsize=128)
def basic_question(question):

    completion = client.chat.completions.create(
        model="MiniMaxAI/MiniMax-M2.7",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ],
    )
    result = completion.choices[0].message.content
    print(f"Result obtained successfully{result}")
    return result

def main():
    question = input("Enter your question: ")
    result = basic_question(question)
    print(result)

if __name__ == "__main__":
    main()
