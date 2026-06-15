import streamlit as st
import requests

# إعداد الصفحة
st.set_page_config(page_title="MRX MOOD", layout="centered")

# إخفاء إيميلك (نظام تسجيل دخول خاص بالمستخدم)
if 'user_email' not in st.session_state:
    st.markdown("<h1 style='text-align: center; color: #ff0000;'>MRX MOOD - LOGIN</h1>", unsafe_allow_html=True)
    user_email = st.text_input("أدخل بريدك الإلكتروني:")
    user_name = st.text_input("أدخل اسمك:")
    if st.button("دخول"):
        if user_email and user_name:
            st.session_state.user_email = user_email
            st.session_state.user_name = user_name
            st.rerun()
    st.stop()

# التصميم الفخم
st.markdown("""
    <style>
        .stApp { background-color: #000; color: #fff; }
        .sidebar .sidebar-content { background: #000; border-left: 1px solid #333; }
        .user-profile { border: 1px solid #333; padding: 15px; border-radius: 15px; text-align: center; margin-bottom: 20px; }
        .msg { padding: 15px; border-radius: 20px; margin: 10px 0; border: 1px solid #333; }
        .mrx-msg { background: #151515; }
    </style>
""", unsafe_allow_html=True)

# القائمة الجانبية (بيانات المستخدم الحالي)
with st.sidebar:
    st.markdown(f"<div class='user-profile'><h3>{st.session_state.user_name}</h3><p>{st.session_state.user_email}</p></div>", unsafe_allow_html=True)
    if st.button("تسجيل خروج"):
        del st.session_state.user_email
        st.rerun()

# واجهة الدردشة
st.header("MRX MOOD")
if "messages" not in st.session_state: st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("اسأل مساعد MRX..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.write(prompt)
    
    # الاتصال بـ API
    try:
        response = requests.post(
            "https://zailtqlrdcukgythlbwq.supabase.co/functions/v1/exos",
            headers={"Authorization": "Bearer exos_7d73425a42b9ebdbca982f04f84d0f267c2f720cf478a28c"},
            json={"message": prompt, "model": "deepseek-ai/DeepSeek-V3.1"}
        )
        reply = response.text
    except:
        reply = "عذراً، حدث خطأ في الاتصال بالخادم."
        
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"): st.write(reply)
