import streamlit as st
import requests
import json

# إعداد الصفحة
st.set_page_config(page_title="MRX MOOD", page_icon="🤖")

# CSS المخصص للألوان والأشكال
st.markdown("""
    <style>
    /* تغيير لون خلفية التطبيق */
    .stApp { background-color: #000; color: #fff; }
    
    /* تنسيق رسائل المستخدم (أحمر) */
    div[data-testid="stChatMessage"][data-author="user"] {
        background-color: #8b0000 !important;
        color: white !important;
        border-radius: 10px;
    }
    
    /* تنسيق رسائل المساعد (أبيض) */
    div[data-testid="stChatMessage"][data-author="assistant"] {
        background-color: #ffffff !important;
        color: black !important;
        border-radius: 10px;
    }
    
    /* تنسيق صندوق الكود (أسود) */
    pre {
        background-color: #1c1c1c !important;
        color: #ffffff !important;
        border: 1px solid #ff0000 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("MRX MOOD 🤖")

# تهيئة المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة
for msg in st.session_state.messages:
    # استخدام أيقونات مخصصة
    avatar = "👤" if msg["role"] == "user" else "🤖"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

# منطقة الإدخال
if prompt := st.chat_input("اسأل مساعد MRX..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🤖"):
        # الرد المنطقي
        if "من صنعك" in prompt:
            response = "تم تطويري بواسطة ماجد حاكم الدراك."
        else:
            # هنا تضع دالة الاتصال بالـ API الخاصة بك
            response = "هذا مثال لكود:\n```python\nprint('Hello MRX')\n```"
        
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
