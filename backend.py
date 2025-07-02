
import os
from openai import OpenAI

# إنشاء عميل GPT
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# توليد التوصية بناءً على وصف المستخدم ولغته
def generate_sport_recommendation(user_answers, language="ar"):
    if language == "ar":
        prompt = "بناءً على إجابات المستخدم التالية، اقترح له رياضة مناسبة تمامًا لشخصيته واهتماماته وخبرته السابقة، ووضح السبب:\n\n" + user_answers
    else:
        prompt = "Based on the user's answers below, recommend the most suitable sport that matches their personality, interests, and experience. Explain why:\n\n" + user_answers

    # إرسال الطلب إلى GPT
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
        ]
    )

    return response.choices[0].message.content
