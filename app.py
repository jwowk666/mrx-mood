import streamlit as st
import requests

# 1. إعداد الصفحة وتصميمها (CSS)
st.set_page_config(page_title="MRX MOOD", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; }
    /* تصميم المحادثة */
    .user-msg { background: linear-gradient(to left, #ff0000, #800); padding: 15px; border-radius: 20px; margin: 10px 0; align-self: flex-start; }
    .mrx-msg { background: #151515; border: 1px solid #333; padding: 15px; border-radius: 20px; margin: 10px 0; align-self: flex-end; }
    /* إخفاء شعار ستريم ليت */
    #MainMenu, footer, header { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

# 2. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.markdown("### رياض صادق")
    st.caption("ryadsadq806@gmail.com")
    st.divider()
    st.write("مطور بواسطة: ماجد حاكم الدراك")

# 3. عرض المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "مرحباً بك، كيف يمكنني مساعدتك اليوم؟"}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 4. منطقة الإدخال (بدون ملفات أو صور)
if prompt := st.chat_input("اسأل مساعد MRX..."):
    # إضافة رسالة المستخدم
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # الرد من الخادم (الـ API الخاص بك)
    with st.chat_message("assistant"):
        with st.spinner("جاري التفكير..."):
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
                    }
                )
                answer = response.text if response.status_code == 200 else "حدث خطأ في الاتصال."
            except:
                answer = "عذراً، الخادم لا يستجيب حالياً."
            
            st.markdown(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})
