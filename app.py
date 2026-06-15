import streamlit as st
import requests

# [إعدادات الصفحة والـ CSS هنا]
st.set_page_config(page_title="MRX MOOD", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; }
    /* تنسيق زر الإدخال */
    div[data-testid="stChatInput"] { border: 1px solid #ff0000; border-radius: 20px; }
    </style>
""", unsafe_allow_html=True)

st.title("MRX MOOD 🤖")

# عرض المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- منطقة الإدخال المطورة ---
# نضع زر "+" والقائمة المنسدلة في نفس سطر الإدخال
col1, col2 = st.columns([0.1, 0.9])

with col1:
    # إنشاء القائمة المنسدلة (Popover)
    with st.popover("➕"):
        st.write("📂 **المعرض**")
        st.write("📷 **الكاميرا**")
        st.write("📎 **ملفات**")
        st.write("📚 **المجموعات**")
        st.write("🎨 **إنشاء صورة**")
        st.write("🔭 **بحث معمق**")

with col2:
    # حقل الإدخال
    prompt = st.text_input("", placeholder="اسأل مساعد MRX...", key="input")

if st.button("إرسال"):
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        # [منطق الاتصال بالـ API يوضع هنا]
        st.rerun()
