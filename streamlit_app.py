# streamlit_app.py

import streamlit as st
from backend import generate_sport_recommendation
from PIL import Image, ImageDraw, ImageFont
import io
import pyperclip

st.set_page_config(page_title="Sport Recommender", layout="centered")

st.title("🔍 اكتشف الرياضة المناسبة لك")
st.markdown("أجب على الأسئلة التالية وسنقترح لك رياضة تناسب شخصيتك.")

# اختيار اللغة
language = st.selectbox("اختر اللغة", ["العربية", "English"])
lang_code = "ar" if language == "العربية" else "en"

# نموذج الأسئلة
user_answers = ""
questions = [
    "1. هل سبق أن مارست رياضة من قبل؟",
    "2. كيف تصف نشاطك خلال يومك؟",
    "3. هل تستمتع بالتحديات الجسدية أو الذهنية؟",
    "4. أي من هذه البيئات تفضّل أن تتواجد فيها؟",
    "5. ما مدى استمتاعك بالعمل الجماعي؟",
    "6. هل تفضّل المغامرة أم الروتين؟",
    "7. كيف تقضي أوقات فراغك عادة؟",
    "8. هل تميل إلى التفكير الاستراتيجي أم التنفيذ المباشر؟",
    "9. كيف تتعامل مع المخاطرة؟",
    "10. ما نوع الجهد الذي يستهويك أكثر؟",
    "11. هل تحب المنافسة أم التعاون؟",
    "12. كيف تتفاعل مع الضغط؟",
    "13. هل تحب الألعاب الفردية أم الجماعية؟",
    "14. ما الذي يحفزك للاستمرار؟",
    "15. هل تفضّل الأنشطة الداخلية أم الخارجية؟",
    "16. ما شعورك تجاه الارتفاعات أو السرعة؟",
    "17. هل تحب استخدام أدوات وتجهيزات؟",
    "18. هل جربت التأمل أو الأنشطة الذهنية؟",
    "19. كيف تصف مستوى لياقتك الحالي؟",
    "20. أخبرنا شيئًا عن علاقتك بالرياضة أو هدفك منها."
]

st.markdown("### ✍️ الأسئلة:")
for q in questions:
    answer = st.text_input(q, key=q)
    user_answers += f"{q}\n{answer}\n\n"

# زر توليد التوصية
if st.button("🎯 اعرض التوصية"):
    with st.spinner("يتم تحليل إجاباتك..."):
        recommendation = generate_sport_recommendation(user_answers, language=lang_code)
        st.success("✨ توصيتك الرياضية:")
        st.markdown(recommendation)

        # 1. زر نسخ النتيجة
        if st.button("📋 انسخ التوصية"):
            pyperclip.copy(recommendation)
            st.toast("✅ تم نسخ التوصية!")

        # 2. زر رابط عام (placeholder فقط)
        if st.button("🔗 مشاركة رابط النتيجة"):
            st.info("🔧 سيتم تفعيل هذه الميزة لاحقًا باستخدام TinyURL أو Firebase.")

        # 3. زر دعوة صديق
        if st.button("👥 دعوة صديق يجاوب"):
            st.write("انسخ الرابط وأرسله لصديقك ليجرب الأسئلة:")
            st.code("https://your-app-url.com")  # غيّره لاحقًا بالرابط الحقيقي

        # 4. زر تحويل التوصية إلى صورة
        if st.button("🖼️ حوّل التوصية إلى صورة"):
            img = Image.new('RGB', (800, 600), color=(255, 255, 255))
            draw = ImageDraw.Draw(img)
            font = ImageFont.load_default()
            draw.text((10, 10), recommendation, fill=(0, 0, 0), font=font)
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            st.image(buf.getvalue(), caption="توصيتك كصورة", use_column_width=True)
