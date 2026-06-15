import streamlit as st
import requests

# إعداد الصفحة
st.set_page_config(page_title="MRX MOOD", page_icon="🤖")

# CSS لإعطاء طابع أسود وأحمر فخم
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; }
    /* تنسيق صندوق المحادثة */
    div[data-testid="stChatMessage"] { background-color: #151515 !important; border-left: 3px solid #ff0000; }
    </style>
""", unsafe_allow_html=True)

st.title("MRX MOOD 🤖")

# إدارة المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# الإدخال
if prompt := st.chat_input("اسأل مساعد MRX..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # 1. منطق الرد على سؤال المطور
        if "من صنعك" in prompt or "من مطورك" in prompt:
            response = "أنا مساعد MRX، تم تطويري بواسطة: ماجد حاكم الدراك."
        
        # 2. منطق الاتصال بالـ API (مدمج)
        else:
            try:
                # محاكاة الاتصال بالخادم الخاص بك
                response = "هذا مثال لكود بايثون:\n\n
http://googleusercontent.com/immersive_entry_chip/0

### لماذا هذا الحل هو الأفضل؟

1.  **المربعات البرمجية:** باستخدام `st.markdown` مع كتابة الكود داخل (```python ... ```)، سيقوم Streamlit **تلقائياً** بإنشاء مربع أسود للكود مع زر "نسخ" (Copy) في الزاوية العلوية كما طلبت في الصورة، ولن يظهر لك أي شيء "مش حلو".
2.  **الرد الذكي:** أضفت شرطاً `if "من صنعك" in prompt:` لجعل المساعد يرد باسم المطور فوراً.
3.  **إزالة الإزعاج:** استبدلت حقل الإدخال العادي بـ `st.chat_input`، وهو الحقل الذي يظهر في الأسفل دائماً مثل Gemini و ChatGPT، وهو أجمل بكثير من `text_input` والزر المنفصل.
4.  **التنسيق:** الـ CSS المضاف يجعل خلفية رسائل المساعد باللون `#151515` مع خط أحمر جانبي، مما يعطيه هيبة وفخامة.

**نصيحة تقنية:**
عندما يقوم المساعد بكتابة كود في المستقبل، تأكد دائماً أنك تضع الكود داخل علامات التجزئة (` ``` `) في الـ `response` الخاص بك، وسيقوم Streamlit بتحويله إلى مربع كود احترافي (مع تحديد اللغة مثل `python` أو `html`) تلقائياً.

هل تريد مني تعديل "رسالة الترحيب" أو إضافة أوامر أخرى للمساعد؟
