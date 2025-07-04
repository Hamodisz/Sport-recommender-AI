import json
import streamlit as st
from backend import generate_sport_recommendation

def load_questions(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

# إعداد الصفحة
st.set_page_config(page_title="Sport Recommender", layout="centered")

# اختيار اللغة
lang = st.radio("اختر اللغة / Choose language", ["العربية", "English"])

# تحميل الأسئلة حسب اللغة
if lang == "العربية":
    questions = load_questions("arabic_questions.json")
    submit_label = "احصل على توصيتك"
    title = "استخدم الذكاء الاصطناعي لمعرفة الرياضة المناسبة لك 🧠🏅"
else:
    questions = load_questions("english_questions.json")
    submit_label = "Find Your Sport"
    title = "Use AI to Discover Your Ideal Sport 🧠🏅"

st.title(title)

answers = {}
for q in questions:
    if "options" in q:
        answers[q["question"]] = st.radio(q["question"], q["options"])
    else:
        answers[q["question"]] = st.text_input(q["question"])

if st.button(submit_label):
    with st.spinner("⏳ جاري توليد التوصية..." if lang == "العربية" else "Generating recommendation..."):
        recommendation = generate_sport_recommendation(answers, lang)
        st.success(recommendation)