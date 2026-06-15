import streamlit as st
import requests

# إعداد الصفحة
st.set_page_config(page_title="MRX MOOD", layout="centered")

# CSS لإعطاء طابع "فخم" وتأثيرات حمراء
st.markdown("""
    <style>
    .stApp { background-color: #000; }
    .msg-box { background: #151515; border: 1px solid #ff0000; border-radius: 10px; padding: 15px; margin: 10px 0; color: #fff; }
    .code-box { background: #000 !important; border: 1px solid #ff0000 !important; }
    div[data-testid="stChatMessage"] { background-color: #000 !important; }
    </style>
""", unsafe_allow_html=True)

# 1. نظام تسجيل الدخول البسيط
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 تسجيل الدخول إلى MRX")
    email = st.text_input("أدخل البريد الإلكتروني:")
    if st.button("دخول"):
        if email:
            st.session_state.logged_in = True
            st.rerun()
    st.stop()

# 2. الواجهة الرئيسية
st.title("MRX MOOD")

if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل
for i, msg in enumerate(st.session_state.messages):
    with st.chat_message("assistant" if msg["role"] == "assistant" else "user"):
        st.markdown(msg["content"])
        
        # إذا كانت رسالة من المساعد، أضف زر النسخ
        if msg["role"] == "assistant":
            st.button(f"نسخ الإجابة {i}", key=f"copy_{i}")

# حقل الإدخال
if prompt := st.chat_input("اسأل مساعد MRX..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # هنا محاكاة للرد (استبدل هذا بمنطق الـ API الخاص بك)
    response = "هذا مثال لكود برمجي:\n\n```python\nprint('Hello MRX')\n```"
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()
