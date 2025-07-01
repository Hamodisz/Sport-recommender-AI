
import streamlit as st
import openai
import os

st.set_page_config(page_title="Sport Recommender", layout="centered")

# 🟡 اختيار اللغة
language = st.selectbox("اختر اللغة / Choose Language", ["العربية", "English"])

# 🟢 إدخال مفتاح OpenAI
api_key = st.text_input("🔐 أدخل مفتاح OpenAI API", type="password")
if api_key:
    openai.api_key = api_key
    os.environ["OPENAI_API_KEY"] = api_key

# 🟣 الأسئلة
questions = [
    "لو كانت عندك ساعة فراغ بعد يوم طويل، أي نوع من النشاطات ترتاح له أكثر؟",
    "أي وصف يطابق شعورك تجاه المغامرات؟",
    "هل سبق وجربت رياضة من قبل واستمتعت فيها؟",
    "لو كنت في عطلة نهاية الأسبوع، أي نوع من التجارب تفضل؟",
    "أي من التالي يمثل بيئتك الحالية؟",
    "كيف تصف مستوى لياقتك البدنية حاليًا؟",
    "هل تفضل التحديات الفردية أم الجماعية؟",
    "كيف تتعامل مع الخوف أو الضغط؟",
    "هل تحب المنافسة؟",
    "أي من التالي يعجبك أكثر؟",
    "كيف تشوف نفسك من ناحية الصبر؟",
    "هل تحب تتعلم مهارة جديدة حتى لو كانت صعبة؟",
    "هل تعتبر نفسك اجتماعي أو انعزالي؟",
    "هل تفضل تخطيط اليوم بدقة أو تروح مع التيار؟",
    "هل تحب الطبيعة؟",
    "هل تفضل الرياضات في الأماكن المغلقة أم المفتوحة؟",
    "هل تحب اللعب بسرعة أو براحة؟",
    "أي من التالي يمثل أسلوبك في الحياة؟",
    "هل تستمتع بالتكرار والتطوير أم تحب التنوع والتغيير؟",
    "هل تعتبر التحكم في النفس نقطة قوة عندك؟"
]

answers = []

# 📝 عرض الأسئلة كمربعات اختيار
for q in questions:
    answer = st.radio(q, ["أ", "ب", "ج", "د", "غير ذلك - أكتب رأيك"], key=q)
    answers.append(answer)

# 🔘 زر الإرسال
if st.button("🔍 احصل على التوصية الرياضية"):
    with st.spinner("يتم تحليل إجاباتك..."):

        messages = [
            {"role": "system", "content": "أنت مساعد ذكي متخصص في اقتراح الرياضة المناسبة بناءً على شخصية المستخدم. استخدم علم النفس الرياضي ونظريات الشخصية."},
            {"role": "user", "content": f"الإجابات: {answers}. أعطني اسم رياضة واحدة تناسبه ولماذا."}
        ]

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            result = response.choices[0].message.content
            st.success("✨ التوصية الرياضية:")
            st.write(result)
        except Exception as e:
            st.error(f"❌ حدث خطأ: {e}")
