import streamlit as st
import requests
import json
import re

# إعداد الصفحة
st.set_page_config(page_title="MRX MOOD", page_icon="🤖")

st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; }
    </style>
""", unsafe_allow_html=True)

st.title("MRX MOOD 🤖")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

def get_clean_response(user_input):
    # منطق الرد على المطور
    if "من صنعك" in user_input or "من مطورك" in user_input:
        return "أنا مساعد MRX، تم تطويري بواسطة المبرمج: ماجد حاكم الدراك."

    # منطق الـ API (تأكد أن الكود داخل علامات ``` )
    try:
        # هنا اتصال الـ API الخاص بك... 
        # تأكد أن الرد الذي يعود لك يوضع داخل علامات الـ markdown
        # مثال: full_text = "```python\nprint('Hello')\n```"
        return "```python\n# مثال كود برمجى\nprint('مرحباً بك في MRX MOOD')\n```"
    except:
        return "حدث خطأ في الاتصال."

if prompt := st.chat_input("اسأل مساعد MRX..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = get_clean_response(prompt)
        # عند عرض الرد، استخدم markdown فقط
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
