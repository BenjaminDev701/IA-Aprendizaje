from openai.types.responses import response
import __main__
from openai import APIConnectionError
from openai import OpenAI, AuthenticationError, RateLimitError, APITimeoutError
from dotenv import load_dotenv

load_dotenv()


def call_ai(question: str) -> str:
    client = OpenAI()
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ],
            max_tokens=300,
            temperature=0.7
        )
        return response.choices[0].message.content

    except AuthenticationError:
        print("API KEY invalida")
        raise SystemExit(1)

    except RateLimitError:
        print("Limite excedido, espera...")
        raise
    except APIConnectionError:
        print("Sin conexion revisa tu internet")

    except Exception as e:
        print(f"error inesperado {type(e).__name__}: {e}")


if __name__ == "__main__":
    response = call_ai("Cual es el area mejor pagada de TI")

    print(f"AI: {response}")
