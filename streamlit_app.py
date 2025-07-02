
import streamlit as st
from backend import generate_sport_recommendation
import base64
import os
from shared.utils import save_to_csv, generate_image

st.set_page_config(page_title="Sport Recommender", layout="centered")

st.title("🏅 اكتشف الرياضة المناسبة لك")
st.markdown("أجب على الأسئلة التالية وسنقترح لك رياضة تناسب شخصيتك.")

# اختيار اللغة
language = st.selectbox("اختر اللغة / Choose Language", ["العربية", "English"])
lang_code = "ar" if language == "العربية" else "en"

# الأسئلة
questions = [
    "1. هل سبق أن مارست رياضة من قبل؟",
    "2. كيف تصف مستوى نشاطك اليومي؟",
    "3. ما الذي يجذبك أكثر؟",
    "4. كيف تفضل قضاء وقت فراغك؟",
    "5. أي نوع من التمارين تستمتع به؟",
    "6. كيف تصف شخصيتك في كلمة؟",
    "7. ما الذي تبحث عنه من الرياضة؟",
    "8. هل تحب المنافسة؟",
    "9. هل تفضل الأنشطة الفردية أم الجماعية؟",
    "10. ما البيئة التي تفضلها للتدريب؟",
    "11. كيف تحب أن تبدأ يومك؟",
    "12. هل تعتبر نفسك مغامرًا؟",
    "13. ما نوع التعب الذي تفضله؟",
    "14. كيف تحفّز نفسك؟",
    "15. هل تفضل التحديات العقلية أم البدنية؟",
    "16. كم مرة تتمرن بالأسبوع؟",
    "17. هل تحب السفر والاستكشاف؟",
    "18. ما رأيك بالالتزام طويل الأمد؟",
    "19. ما هدفك الرئيسي من ممارسة الرياضة؟",
    "20. كم من الوقت تقضي على شاشة الجوال يوميًا؟"
]

answers = []
for q in questions:
    a = st.text_input(q)
    answers.append(f"{q}
{a}
")

# توليد التوصية
if st.button("🎯 احصل على التوصية"):
    all_answers = "
".join(answers)
    recommendation = generate_sport_recommendation(all_answers, language=lang_code)

    st.subheader("🎽 توصيتك الرياضية:")
    st.success(recommendation)

    # حفظ في CSV
    save_to_csv(all_answers, recommendation)

    # زر النسخ
    st.markdown("### 📋 نسخ النتيجة:")
    st.code(recommendation, language=None)
    st.button("📋 انسخ", on_click=st.experimental_set_query_params, args=(dict(result=recommendation),))

    # رابط عام
    st.markdown("### 🔗 شارك النتيجة مع الآخرين:")
    share_url = f"https://sport-recommender-ai.streamlit.app/?result={base64.urlsafe_b64encode(recommendation.encode()).decode()}"
    st.write(share_url)

    # زر دعوة صديق
    st.markdown("### 👥 دعوة صديق:")
    invite_url = "https://sport-recommender-ai.streamlit.app/"
    st.write(invite_url)

    # توليد صورة
    st.markdown("### 🖼️ تحويل النتيجة إلى صورة:")
    if st.button("حوّل إلى صورة"):
        img_path = generate_image(recommendation)
        with open(img_path, "rb") as img_file:
            btn = st.download_button(
                label="📥 تحميل الصورة",
                data=img_file,
                file_name="recommendation.png",
                mime="image/png"
            )
