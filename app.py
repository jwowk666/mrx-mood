import streamlit as st
import requests

# إعداد الصفحة
st.set_page_config(page_title="MRX MOOD", layout="wide")

# CSS للتصميم الفخم (أسود وأحمر)
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; }
    .stTextInput>div>div>input { background-color: #151515 !important; color: white !important; border: 1px solid #ff0000 !important; }
    </style>
""", unsafe_allow_html=True)

st.title("MRX MOOD 🤖")

# القائمة الجانبية
with st.sidebar:
    st.markdown("### رياض صادق")
    st.write("مطور بواسطة: ماجد حاكم الدراك")

# إدارة المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل القديمة
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# استخدام text_input بدلاً من chat_input لتجنب الخطأ
prompt = st.text_input("اسأل مساعد MRX:", key="user_input")

if st.button("إرسال"):
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # الاتصال بالـ API
        try:
            response = requests.post(
                "https://zailtqlrdcukgythlbwq.supabase.co/functions/v1/exos",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer exos_7d73425a42b9ebdbca982f04f84d0f267c2f720cf478a28c"
                },
                json={
                    "message": prompt,
                    "model": "deepseek-ai/DeepSeek-V3.1"
                },
                timeout=20
            )
            answer = response.text if response.status_code == 200 else "خطأ في الاتصال بالخادم."
        except:
            answer = "عذراً، تعذر الوصول للسيرفر."

        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.rerun() # تحديث الصفحة لعرض الرسالة الجديدة
