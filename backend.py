import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_sport_recommendation(user_answers, language="ar"):
    if language == "ar":
        prompt = f"""بناءً على إجابات المستخدم التالية، اقترح له رياضة مناسبة تمامًا لشخصيته واهتماماته وخبرته السابقة. ووضح السبب:
{user_answers}"""
    else:
        prompt = f"""Based on the user's answers below, recommend the most suitable sport that matches their personality, interests, and experience. Explain why:
{user_answers}"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}]
    )

    return response.choices[0].message.content
