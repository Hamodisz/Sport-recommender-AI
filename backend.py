import openai
import os

def generate_sport_recommendation(answers, lang):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = "الأسئلة وإجابات المستخدم:
" if lang == "العربية" else "User's answers:
"
    for question, answer in answers.items():
        prompt += f"{question}: {answer}\n"

    prompt += "\nبناءً على هذه المعلومات، ما هي أفضل رياضة لهذا الشخص ولماذا؟" if lang == "العربية" else "\nBased on this information, what is the ideal sport for this person and why?"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that recommends the perfect sport."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()