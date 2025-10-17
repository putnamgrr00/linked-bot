import os
from openai import OpenAI

def call_llm(prompt: str) -> str:
    """
    Call OpenAI's GPT-4o model using your API key from environment variable OPENAI_API_KEY.
    """
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", ""))

    response = client.chat.completions.create(
        model="gpt-4o",  # you can also use "gpt-4-turbo" if you prefer
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    test_prompt = "Hello, how are you?"
    print("Making call...")
    print(call_llm(test_prompt))
