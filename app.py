import streamlit as st
import requests

# 1. إعداد الصفحة
st.set_page_config(page_title="MRX MOOD", page_icon="🤖")

# 2. تنسيق الألوان (أسود وأحمر)
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; }
    div[data-testid="stButton"] button { background-color: #ff0000; color: white; border: none; }
    </style>
""", unsafe_allow_html=True)

st.title("MRX MOOD 🤖")

# 3. تخزين الرسائل
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. عرض المحادثة
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 5. حقل الإدخال (تم تغييره ليكون متوافقاً تماماً)
prompt = st.text_input("اكتب رسالتك هنا...", key="input_text")

if st.button("إرسال"):
    if prompt:
        # إضافة رسالة المستخدم
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # الاتصال بالـ API
        try:
            response = requests.post(
                "https://zailtqlrdcukgythlbwq.supabase.co/functions/v1/exos",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": "Bearer exos_7d73425a42b9ebdbca982f04f84d0f267c2f720cf478a28c"
                },
                json={"message": prompt, "model": "deepseek-ai/DeepSeek-V3.1"}
            )
            answer = response.text if response.status_code == 200 else "خطأ في الاتصال."
        except:
            answer = "تعذر الوصول للخادم."
        
        # إضافة رد المساعد
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.rerun()
