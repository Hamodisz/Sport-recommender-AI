
import streamlit as st
from backend import generate_sport_recommendation

# Arabic and English questions embedded directly
arabic_questions = [
    {"question": "ما هو هدفك الأساسي من ممارسة الرياضة؟", "options": ["تحسين اللياقة", "بناء عضلات", "المتعة", "التحدي", "تقليل التوتر"]},
    {"question": "أين تفضل التمرين؟", "options": ["الهواء الطلق", "النادي", "المنزل", "لا فرق"]},
    {"question": "هل تحب الرياضات التي تتطلب تركيزاً ذهنياً؟", "options": ["نعم", "لا", "أحياناً"]},
    {"question": "ما مدى حبك للمنافسة؟", "options": ["أحبها جداً", "معتدل", "لا أهتم"]},
    {"question": "كيف تصف مستوى لياقتك الحالي؟", "options": ["عالية", "متوسطة", "منخفضة"]},
    {"question": "هل تفضل الرياضات الجماعية أم الفردية؟", "options": ["جماعية", "فردية", "لا يهم"]},
    {"question": "هل تعاني من أي إصابات؟", "options": ["نعم", "لا"]},
    {"question": "ما مدى مرونتك الجسدية؟", "options": ["عالية", "متوسطة", "ضعيفة"]},
    {"question": "هل تحب تعلم مهارات جديدة؟", "options": ["نعم", "أحياناً", "لا"]},
    {"question": "كم مرة تستطيع التمرن أسبوعيًا؟", "options": ["يوميًا", "٣-٥ مرات", "١-٢ مرات"]},
    {"question": "هل تحب الرياضات القتالية؟", "options": ["نعم", "لا", "لم أجرب"]},
    {"question": "هل تستمتع بالأنشطة التي تحتوي على مغامرة؟", "options": ["نعم", "أحيانًا", "لا"]},
    {"question": "هل سبق وأن مارست رياضة بشكل منتظم؟", "options": ["نعم", "لا"]},
    {"question": "ما أكثر ما يحفزك للاستمرار؟", "options": ["النتائج", "المتعة", "المنافسة"]},
    {"question": "هل تفضل التمارين المكثفة أم الهادئة؟", "options": ["مكثفة", "هادئة", "حسب المزاج"]},
    {"question": "هل تفضل أن يكون التمرين ضمن جدول صارم؟", "options": ["نعم", "لا", "أحيانًا"]},
    {"question": "هل تهتم بتقوية العقل مثل الجسد؟", "options": ["نعم", "لا"]},
    {"question": "هل ترغب في رياضة تساعدك على التركيز؟", "options": ["نعم", "لا", "ربما"]},
    {"question": "هل تحب الرياضات الخارجية في الطبيعة؟", "options": ["نعم", "لا", "أحيانًا"]},
    {"question": "هل تحب الرياضات الإبداعية أو الرقص؟", "options": ["نعم", "لا", "لم أجرب"]}
]

english_questions = [
    {"question": "What is your main goal in sports?", "options": ["Improve fitness", "Build muscle", "Fun", "Challenge", "Stress relief"]},
    {"question": "Where do you prefer to train?", "options": ["Outdoors", "Gym", "Home", "No preference"]},
    {"question": "Do you enjoy mentally challenging sports?", "options": ["Yes", "No", "Sometimes"]},
    {"question": "How competitive are you?", "options": ["Very", "Moderate", "Not much"]},
    {"question": "How fit are you currently?", "options": ["High", "Medium", "Low"]},
    {"question": "Do you prefer team or solo sports?", "options": ["Team", "Solo", "Doesn’t matter"]},
    {"question": "Do you have any injuries?", "options": ["Yes", "No"]},
    {"question": "How flexible are you?", "options": ["High", "Moderate", "Low"]},
    {"question": "Do you enjoy learning new skills?", "options": ["Yes", "Sometimes", "No"]},
    {"question": "How often can you train weekly?", "options": ["Daily", "3-5 times", "1-2 times"]},
    {"question": "Do you like combat sports?", "options": ["Yes", "No", "Never tried"]},
    {"question": "Do you enjoy adventurous activities?", "options": ["Yes", "Sometimes", "No"]},
    {"question": "Have you trained regularly before?", "options": ["Yes", "No"]},
    {"question": "What motivates you most?", "options": ["Results", "Fun", "Competition"]},
    {"question": "Do you prefer intense or calm workouts?", "options": ["Intense", "Calm", "Depends"]},
    {"question": "Do you like structured training plans?", "options": ["Yes", "No", "Sometimes"]},
    {"question": "Do you care about mental strength too?", "options": ["Yes", "No"]},
    {"question": "Would you like focus-enhancing sports?", "options": ["Yes", "No", "Maybe"]},
    {"question": "Do you enjoy nature-based sports?", "options": ["Yes", "No", "Sometimes"]},
    {"question": "Do you like creative sports or dance?", "options": ["Yes", "No", "Never tried"]}
]

# UI
st.set_page_config(page_title="Sport Recommender", layout="centered")

lang = st.radio("اختر اللغة / Choose language", ["العربية", "English"])
if lang == "العربية":
    questions = arabic_questions
    submit_label = "احصل على التوصية"
    title = "أجب على الأسئلة التالية وسيتم ترشيح الرياضة المناسبة لك باستخدام الذكاء الاصطناعي 🤖"
else:
    questions = english_questions
    submit_label = "Get Recommendation"
    title = "Answer the questions below to get your ideal sport recommendation using AI 🤖"

st.title("🏅 Sport Recommender")
st.write(title)

answers = {}
for q in questions:
    answers[q["question"]] = st.radio(q["question"], q["options"])

if st.button(submit_label):
    with st.spinner("⏳"):
        result = generate_sport_recommendation(answers, lang)
        st.success(result)
