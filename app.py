import streamlit as st
import requests
import json
import re

# إعداد الصفحة لتكون متوافقة مع جوالك (تصميم مظلم)
st.set_page_config(page_title="MRX MOOD", page_icon="🤖", layout="centered")

# تنسيق CSS ليكون مطابقاً لتصميمك
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; }
    .stTextInput>div>div>input { border-radius: 20px !important; border: 1px solid #333 !important; }
    .msg { padding: 15px; border-radius: 20px; margin: 10px 0; max-width: 80%; }
    .user-msg { background: linear-gradient(to left, #ff0000, #800); color: white; margin-left: auto; }
    .mrx-msg { background: #151515; border: 1px solid #333; color: #fff; }
    </style>
""", unsafe_allow_html=True)

# العنوان الجانبي (Sidebar)
with st.sidebar:
    st.markdown("### رياض صادق")
    st.caption("ryadsadq806@gmail.com")
    st.divider()
    st.info("مطور بواسطة: ماجد حاكم الدراك")

st.title("MRX MOOD 🤖")

# تهيئة سجل المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "مرحباً بك، كيف يمكنني مساعدتك اليوم؟"}]

# عرض الرسائل السابقة
for msg in st.session_state.messages:
    css_class = "user-msg" if msg["role"] == "user" else "mrx-msg"
    st.markdown(f'<div class="msg {css_class}">{msg["content"]}</div>', unsafe_allow_html=True)

# دالة الاتصال بالـ API
def get_deepseek_response(user_input):
    try:
        s = requests.Session()
        # جلب التوكنات (نفس المنطق الذي استخدمته)
        r = s.get("https://deep-seek.ai", headers={'User-Agent': 'Mozilla/5.0'})
        c1 = s.cookies.get('XSRF-TOKEN')
        c2 = re.search(r'csrf-token["\s]+content=["\']([^"\']+)', r.text).group(1)
        
        headers = {
            'Content-Type': 'application/json',
            'X-CSRF-TOKEN': c2,
            'Cookie': f'XSRF-TOKEN={c1}',
            'X-Developer': '@HackerExos'
        }
        
        payload = {
            "model": "deepseek/deepseek-v3.2",
            "messages": [{"role": "user", "content": user_input}],
            "stream": False # لتبسيط العرض في Streamlit
        }
        
        res = s.post("https://deep-seek.ai/api/chat", headers=headers, json=payload)
        return res.text
    except Exception as e:
        return "حدث خطأ في الاتصال بالسيرفر."

# حقل الإدخال
if prompt := st.chat_input("اسأل مساعد MRX..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.rerun()

# تنفيذ الرد
if st.session_state.messages[-1]["role"] == "user":
    response = get_deepseek_response(st.session_state.messages[-1]["content"])
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()
