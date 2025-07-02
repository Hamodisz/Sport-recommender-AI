import streamlit as st
from backend.main import generate_sport_recommendation
import base64
import os

from shared.utils import save_to_csv, generate_image, get_smart_questions

st.set_page_config(page_title="Sport Recommender", layout="centered")

# العنوان والوصف
st.title("🥇 اكشف الرياضة المناسبة لك")
st.markdown("أجب على الأسئلة التالية وسنقترح لك رياضة تناسب شخصيتك.")

# اختيار اللغة
language = st.selectbox("اختر اللغة / Choose Language", ["العربية", "English"])
lang_code = "ar" if language == "العربية" else "en"

# استيراد الأسئلة الذكية
questions = get_smart_questions()
answers = []

# عرض الأسئلة وتجميع الإجابات
for q in questions:
    a = st.text_input(q)
    answers.append(f"{q} {a}")

# توليد التوصية
if st.button("🔍 احصل على التوصية"):
    all_answers = "\n".join(answers)
    recommendation = generate_sport_recommendation(all_answers, language=lang_code)

    st.subheader("🌱 توصيك الرياضية:")
    st.success(recommendation)

    # حفظ البيانات في CSV
    save_to_csv(all_answers, recommendation)

    # نسخ التوصية
    st.markdown("### 📋 انسخ النتيجة:")
    st.code(recommendation, language=None)