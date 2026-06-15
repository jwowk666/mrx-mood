import streamlit as st
import requests
import json
import re

# إعداد الصفحة
st.set_page_config(page_title="MRX MOOD", page_icon="🤖", layout="centered")

# CSS للتصميم المظلم (الأسود والأحمر)
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; }
    .msg { padding: 15px; border-radius: 20px; margin: 10px 0; max-width: 80%; }
    .user-msg { background: linear-gradient(to left, #ff0000, #800); color: white; margin-left: auto; }
    .mrx-msg { background: #151515; border: 1px solid #333; color: #fff; }
    </style>
""", unsafe_allow_html=True)

# العنوان الجانبي
with st.sidebar:
    st.markdown("### رياض صادق")
    st.caption("ryadsadq806@gmail.com")
    st.divider()
    st.info("مطور بواسطة: ماجد حاكم الدراك")

st.title("MRX MOOD 🤖")

# تهيئة سجل المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "مرحباً بك، كيف يمكنني مساعدتك اليوم؟"}]

# عرض الرسائل
for msg in st.session_state.messages:
    css_class = "user-msg" if msg["role"] == "user" else "mrx-msg"
    st.markdown(f'<div class="msg {css_class}">{msg["content"]}</div>', unsafe_allow_html=True)

# ===================== التعديل الأساسي هنا فقط =====================
# مفتاح API الخاص بك (يجب أن تحصل عليه من deepseek.com)
DEEPSEEK_API_KEY = "sk-your-api-key-here"  # ⚠️ استبدل هذا بمفتاحك الحقيقي

def get_clean_response(user_input):
    """دالة معدلة لاستخدام API الرسمي بدلاً من الاختراق"""
    try:
        url = "https://api.deepseek.com/v1/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }
        
        # نرسل فقط الرسالة الحالية (للبساطة)
        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "user", "content": user_input}
            ],
            "temperature": 0.7,
            "max_tokens": 2000,
            "stream": False  # تبسيط: غير متدفق (غير stream)
        }
        
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            return data['choices'][0]['message']['content']
        else:
            return f"⚠️ خطأ: {response.status_code} - {response.text}"
            
    except Exception as e:
        return f"❌ حدث خطأ في الاتصال: {str(e)}"

# ===================== نهاية التعديل =====================

# حقل الإدخال
if prompt := st.chat_input("اسأل مساعد MRX..."):
    # إضافة رسالة المستخدم
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # الحصول على الرد النظيف
    with st.spinner("جارٍ المعالجة..."):
        response = get_clean_response(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
    
    st.rerun()
