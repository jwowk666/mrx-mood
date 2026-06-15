import streamlit as st
import requests
import json
import base64

# إعداد الصفحة لتكون بوضع "الوضع المظلم" وبشكل فخم
st.set_page_config(page_title="MRX MOOD", page_icon="🤖", layout="centered")

# CSS لتغيير شكل التطبيق ليصبح فخماً جداً (أسود وأحمر)
st.markdown("""
    <style>
    .stApp { background-color: #000; }
    .main { background-color: #000; }
    /* تنسيق صندوق المحادثة */
    .stChatMessage { background: #151515 !important; border: 1px solid #ff0000; border-radius: 15px; }
    /* تنسيق زر الإرسال */
    div[data-testid="stChatInput"] { border: 2px solid #ff0000; border-radius: 20px; }
    </style>
""", unsafe_allow_html=True)

st.title("MRX MOOD 🤖")

# 1. نظام الدخول
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    with st.container():
        email = st.text_input("أدخل البريد الإلكتروني للبدء:")
        if st.button("دخول"):
            st.session_state.logged_in = True
            st.rerun()
    st.stop()

# 2. منطقة رفع الملفات (فوق المحادثة)
uploaded_file = st.file_uploader("📂 ارفع ملف أو صورة لتحليلها", type=['png', 'jpg', 'pdf'])

if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# دالة ذكية لتنقية الرد (إزالة بيانات الـ OpenRouter)
def parse_response(raw_text):
    clean_text = ""
    for line in raw_text.splitlines():
        if line.startswith("data: "):
            try:
                data = json.loads(line[6:])
                if 'choices' in data:
                    clean_text += data['choices'][0]['delta'].get('content', '')
            except: continue
    return clean_text if clean_text else "عذراً، لم أستطع استخراج الرد."

# الإدخال
if prompt := st.chat_input("اسأل مساعد MRX..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # هنا يتم ربط كود الـ API الخاص بك
        # يجب تمرير 'prompt' للـ API واستلام الرد في res_text
        res_text = "..." # ضع هنا نتيجة الـ API الحقيقية
        
        # التنقية
        final_answer = parse_response(res_text)
        
        # العرض مع زر نسخ (Streamlit يضيفه تلقائياً)
        st.markdown(final_answer)
        st.session_state.messages.append({"role": "assistant", "content": final_answer})
