# streamlit_app.py

import streamlit as st
import base64
from backend import generate_sport_recommendation

st.set_page_config(page_title="Sport Recommender", layout="centered")

st.title("🔍 اكتشف الرياضة المناسبة لك")
st.markdown("أجب على الأسئلة التالية وسنقترح لك رياضة تناسب شخصيتك، مع إمكانية مشاركة النتيجة.")

user_answers = ""
user_answers += "1. هل سبق أن مارست رياضة من قبل؟\n" + st.text_input("1. هل سبق أن مارست رياضة من قبل؟") + "\n"
user_answers += "2. ما نوع الأنشطة التي تجذبك؟\n" + st.text_input("2. ما نوع الأنشطة التي تجذبك؟") + "\n"
user_answers += "3. هل تحب الرياضات الفردية أم الجماعية؟\n" + st.text_input("3. هل تحب الرياضات الفردية أم الجماعية؟") + "\n"
user_answers += "4. كم عمرك؟\n" + st.text_input("4. كم عمرك؟") + "\n"
user_answers += "5. هل تفضل النشاطات الحركية أم الذهنية؟\n" + st.text_input("5. هل تفضل النشاطات الحركية أم الذهنية؟") + "\n"
user_answers += "6. هل تحب المنافسة أم الاسترخاء؟\n" + st.text_input("6. هل تحب المنافسة أم الاسترخاء؟") + "\n"
user_answers += "7. ما هو هدفك من ممارسة الرياضة؟\n" + st.text_input("7. ما هو هدفك من ممارسة الرياضة؟") + "\n"

if st.button("🎯 احصل على التوصية"):
    with st.spinner("⏳ يتم تحليل إجاباتك..."):
        recommendation = generate_sport_recommendation(user_answers, language="ar")
        st.success("✅ التوصية الرياضية المناسبة لك:")
        st.markdown(recommendation)

        # زر نسخ النتيجة
        st.code(recommendation, language="text")
        st.button("📋 نسخ النتيجة", on_click=st.experimental_set_query_params, kwargs={"copied": "true"})

        # رابط عام وهمي (قابل للتخصيص لاحقًا)
        st.markdown("🔗 شارك نتيجتك: [رابط مخصص](https://sport-recommender/share?result=12345)")

        # دعوة صديق
        st.markdown("📨 أرسل هذا الرابط لصديقك ليجرب بنفسه: [جرّب الاختبار](https://sport-recommender.com)")

        # تحويل التوصية إلى صورة (بسيطة)
        st.markdown("🖼️ لتحويل التوصية إلى تصميم بصري، التقط لقطة شاشة وشاركها!")