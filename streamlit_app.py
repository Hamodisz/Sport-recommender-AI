import streamlit as st
from backend_folder.backend import generate_sport_recommendation
import base64
import os
from shared_utils import save_to_csv, generate_image, get_smart_questions

# إعداد الصفحة
st.set_page_config(page_title="Sport Recommender", layout="centered")

# العنوان والوصف
st.title("🏅 اكتشف الرياضة المناسبة لك")
st.markdown("أجب على الأسئلة التالية وسنقترح لك رياضة تناسب شخصيتك.")

# اختيار اللغة
language = st.selectbox("اختر اللغة", ["العربية", "English"])
lang_code = "ar" if language == "العربية" else "en"

# استيراد الأسئلة الذكية
questions = get_smart_questions()
answers = []

# عرض الأسئلة وتجميع الإجابات
for q in questions:
    a = st.text_input(f"{q}")
    answers.append(f"{q} {a}")

# توليد التوصية
if st.button("🔍 احصل على التوصية!"):
    all_answers = "\n".join(answers)
    recommendation = generate_sport_recommendation(all_answers, language=lang_code)

    # عرض التوصية
    st.subheader("🎯 وصف الرياضة:")
    st.markdown(recommendation)

    # حفظ النتائج
    save_to_csv(answers, recommendation)

    # توليد صورة
    image_path = generate_image(recommendation)
    with open(image_path, "rb") as img_file:
        img_bytes = img_file.read()
        encoded_img = base64.b64encode(img_bytes).decode()
        st.image(image_path, use_column_width=True)