# streamlit_app.py

import streamlit as st
from backend import generate_sport_recommendation

st.set_page_config(page_title="Sport Recommender", layout="centered")

st.title("🔍 اكتشف الرياضة المناسبة لك")
st.markdown("أجب على الأسئلة التالية وسنقترح لك رياضة تناسب شخصيتك.")

# نموذج الأسئلة
user_answers = ""

user_answers += "1. هل سبق أن مارست رياضة من قبل؟\n" + st.text_input("
