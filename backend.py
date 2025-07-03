
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_sport_recommendation(answers, lang):
    prompt = build_prompt(answers, lang)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{ "role": "user", "content": prompt }]
    )
    return response.choices[0].message["content"]

def build_prompt(answers, lang):
    joined = "\n".join([f"{k}: {v}" for k, v in answers.items()])
    if lang == "العربية":
        return f"بناءً على إجابات المستخدم التالية، اقترح له رياضة واحدة مناسبة تمامًا مع شرح قصير:\n{joined}"
    else:
        return f"Based on the user's answers below, suggest ONE perfect sport with a short explanation:\n{joined}"
