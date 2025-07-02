# streamlit_app.py

import streamlit as st
from backend import generate_sport_recommendation

st.set_page_config(page_title="Sport Recommender", layout="centered")

st.title("🔍 اكتشف الرياضة المناسبة لك")
st.markdown("أجب على الأسئلة التالية وسنقترح لك رياضة تناسب شخصيتك.")

# الأسئلة الذكية (مرحلة أولى)
user_answers = ""

user_answers += "1. هل سبق أن مارست رياضة من قبل؟\n" + st.text_input("هل سبق أن مارست رياضة من قبل؟") + "\n"
user_answers += "2. ما نوع الأنشطة التي تستمتع بها عادة؟\n" + st.text_input("ما نوع الأنشطة التي تستمتع بها؟") + "\n"
user_answers += "3. كيف تصف مستوى لياقتك الحالي؟\n" + st.text_input("مستوى لياقتك الحالي؟") + "\n"
user_answers += "4. ما هو هدفك من ممارسة الرياضة؟\n" + st.text_input("هدفك من ممارسة الرياضة؟") + "\n"
user_answers += "5. هل تفضّل الأنشطة الفردية أم الجماعية؟\n" + st.text_input("فردية أم جماعية؟") + "\n"
user_answers += "6. ما هو عمرك؟\n" + st.text_input("العمر") + "\n"
user_answers += "7. هل لديك أي إصابات أو مشاكل صحية؟\n" + st.text_input("هل لديك إصابات أو مشاكل صحية؟") + "\n"
user_answers += "8. كم عدد الأيام التي ترغب بممارسة الرياضة فيها أسبوعيًا؟\n" + st.text_input("عدد الأيام أسبوعيًا؟") + "\n"

# زر إرسال
if st.button("🎯 احصل على التوصية"):
    with st.spinner("جارٍ تحليل إجاباتك..."):
        recommendation = generate_sport_recommendation(user_answers, language="ar")
        st.success("✅ التوصية الرياضية المناسبة لك:")
        st.markdown(recommendation)
