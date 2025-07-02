
# streamlit_app.py

import streamlit as st
import urllib.parse
from backend import generate_sport_recommendation

st.set_page_config(page_title="Sport Recommender", layout="centered")

st.title("🔍 اكتشف الرياضة المناسبة لك")
st.markdown("أجب على الأسئلة التالية وسنقترح لك رياضة تناسب شخصيتك.")

# نموذج الأسئلة
user_answers = ""
user_answers += "1. هل سبق أن مارست رياضة من قبل؟\n" + st.text_input("هل سبق أن مارست رياضة من قبل؟") + "\n"
user_answers += "2. ما نوع الأنشطة التي تستمتع بها؟\n" + st.text_input("ما نوع الأنشطة التي تستمتع بها؟") + "\n"
user_answers += "3. ما هدفك من ممارسة الرياضة؟\n" + st.text_input("ما هدفك من ممارسة الرياضة؟") + "\n"
user_answers += "4. هل تفضل الرياضات الفردية أم الجماعية؟\n" + st.text_input("هل تفضل الرياضات الفردية أم الجماعية؟") + "\n"
user_answers += "5. كم عمرك؟\n" + st.text_input("كم عمرك؟") + "\n"

# عند الضغط على الزر
if st.button("🔎 اعرض التوصية"):
    with st.spinner("جاري تحليل إجاباتك..."):
        recommendation = generate_sport_recommendation(user_answers, language="ar")
        st.success("✅ الرياضة المناسبة لك:")
        st.markdown(recommendation)

        # مشاركة التوصية
        encoded_result = urllib.parse.quote(recommendation)
        share_url = f"https://sport-recommender-ai.streamlit.app/?result={encoded_result}"

        st.markdown("### شارك النتيجة مع أصدقائك:")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.button("📋 نسخ النتيجة", on_click=st.code, args=(recommendation,))
        with col2:
            st.markdown(f"[🔗 رابط مباشر للنتيجة]({share_url})")
        with col3:
            st.markdown(f"[📨 ادعُ صديق لتجربة الاختبار](https://sport-recommender-ai.streamlit.app)")

        # توليد صورة بسيطة للمشاركة (كنص)
        st.markdown("---")
        st.markdown("### 🖼️ صورة النتيجة للمشاركة:")
        st.image("https://dummyimage.com/600x200/eeeeee/000000&text=" + urllib.parse.quote(recommendation), caption="شاركها على واتساب أو تويتر أو أي مكان")

