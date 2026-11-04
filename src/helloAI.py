from openai.types.responses import response
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI()

response = llm.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Explica que es langchain"
        }
    ]
)

text = response.choices[0].message.content
print(text)
