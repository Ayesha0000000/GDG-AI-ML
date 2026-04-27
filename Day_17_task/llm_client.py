from groq import Groq
from settings import settings


def get_groq_client():
    return Groq(api_key=settings.groq_api_key)


def generate_answer_from_prompt(prompt: str) -> str:
    client = get_groq_client()

    response = client.chat.completions.create(
        model=settings.groq_model_name,
        messages=[
            {"role": "system", "content": "Answer only from context"},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content or ""
