from functools import total_ordering
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
            "content": "puedos decirme hacer un chunks de ia"
        }
    ]
)

text = response.choices[0].message.content
print(text)

print("\n USO DE TOKENS")
print(f"tokens de entrada: {response.usage.prompt_tokens}")
print(f"tokens de salida: {response.usage.completion_tokens}")
print(f"total de tokens: {response.usage.total_tokens}")

cost_input = (response.usage.prompt_tokens / 1_000_000) * 0.15

cost_output = (response.usage.completion_tokens / 1_000_000) * 0.60

total_cost = cost_input + cost_output

print(f"Costo estimado {total_cost:.6f} USD")

print(f"ID de la respuesta{response.id}")
