import streamlit as st
from backend_folder.backend import generate_sport_recommendation

st.set_page_config(page_title="Sport Recommender", layout="centered")

st.title("🏅 Sport Recommender")
st.write("أجب على الأسئلة التالية وسنقترح عليك الرياضة المناسبة لك باستخدام الذكاء الاصطناعي.")

language = st.radio("اختر اللغة", ("ar", "en"))

user_answers = st.text_area("أدخل إجاباتك أو وصف شخصيتك باختصار", height=200)

if st.button("احصل على التوصية"):
    if user_answers.strip() == "":
        st.warning("الرجاء إدخال الإجابات أولاً.")
    else:
        with st.spinner("جاري تحليل إجاباتك..."):
            recommendation = generate_sport_recommendation(user_answers, language=language)
        st.success("🎯 الرياضة المقترحة:")
        st.write(recommendation)