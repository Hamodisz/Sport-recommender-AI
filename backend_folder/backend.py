import os
import openai

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_sport_recommendation(user_answers, language="ar"):
    if language == "ar":
        prompt = "بناءً على إجابات المستخدم التالية، اقترح له رياضة مناسبة تمامًا لشخصيته واهتماماته وخبرته السابقة، ووضح السبب:\n" + user_answers
    else:
        prompt = "Based on the user's answers below, recommend the most suitable sport that matches their personality, interests, and experience. Explain why:\n" + user_answers

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}]
    )
    return response.choices[0].message.content