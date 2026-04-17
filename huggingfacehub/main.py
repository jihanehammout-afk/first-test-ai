import os
import sys
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

def basic_question(args):

    client = InferenceClient(
        api_key=os.environ["HUGGINGFACEHUB_API_TOKEN"],
    )
    print("Client created successfully, we will ask a question: " + str(args[0]))
    completion = client.chat.completions.create(
        model="MiniMaxAI/MiniMax-M2.7",
        messages=[
            {
                "role": "user",
                "content": args[0]
            }
        ],
    )

    return completion.choices[0].message.content

def main():
    question = input("Enter your question: ")
    result = basic_question([question])
    print(result)

if __name__ == "__main__":
    main()
