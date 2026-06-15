import streamlit as st
import requests
import json

st.set_page_config(page_title="MRX MOOD", layout="centered")

# CSS للفخامة
st.markdown("""
    <style>
    .stApp { background-color: #000; }
    .stChatMessage { background: #151515 !important; border: 1px solid #ff0000; }
    </style>
""", unsafe_allow_html=True)

st.title("MRX MOOD 🤖")

# 1. نظام الدخول
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    email = st.text_input("أدخل البريد الإلكتروني للدخول:")
    if st.button("دخول"):
        st.session_state.logged_in = True
        st.rerun()
    st.stop()

# 2. رفع الملفات والصور
uploaded_file = st.file_uploader("ارفع صورة أو ملف ليحللها المساعد", type=['png', 'jpg', 'pdf'])

if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# دالة تنقية النص من أكواد OPENROUTER
def clean_response(response_text):
    full_text = ""
    for line in response_text.splitlines():
        if line.startswith("data: "):
            content = line[6:]
            if content == "[DONE]": break
            try:
                data = json.loads(content)
                text = data['choices'][0]['delta'].get('content', '')
                full_text += text
            except: pass
    return full_text if full_text else "عذراً، لم أستطع قراءة الرد."

# الإدخال
if prompt := st.chat_input("اسأل مساعد MRX..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # هنا يتم الاتصال
    with st.chat_message("assistant"):
        # محاكاة إرسال للـ API (يجب وضع منطق الـ Session الخاص بك هنا)
        # بعد استلام الرد الخام من res.text:
        raw_data = "..." # ضع هنا res.text القادم من الـ API
        clean_text = clean_response(raw_data)
        st.markdown(clean_text)
        st.session_state.messages.append({"role": "assistant", "content": clean_text})
