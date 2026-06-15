import streamlit as st
import requests
import json

# 1. إعداد الصفحة
st.set_page_config(page_title="MRX MOOD", page_icon="🤖")

# 2. تصميم الألوان (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; }
    /* رسائل المستخدم: أحمر */
    div[data-testid="stChatMessage"][data-author="user"] { background-color: #8B0000 !important; color: white !important; }
    /* رسائل المساعد: أبيض */
    div[data-testid="stChatMessage"][data-author="assistant"] { background-color: #FFFFFF !important; color: black !important; }
    /* مربعات الكود: أسود */
    pre { background-color: #111 !important; color: #fff !important; border: 1px solid #ff0000 !important; }
    </style>
""", unsafe_allow_html=True)

st.title("MRX MOOD 🤖")

# 3. إدارة المحادثة
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    avatar = "👤" if msg["role"] == "user" else "🤖"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

# 4. دالة الاتصال بالـ API (المحرك الحقيقي)
def get_ai_response(prompt):
    url = 'https://chat-deep.ai/wp-json/dsc/v1/chat'
    headers = {
        'Content-Type': 'application/json',
        'X-Wp-Nonce': '3c9123ed3a'
    }
    data = {
        "messages": [{"role": "user", "content": prompt}],
        "model": "deepseek-v4-flash",
        "thinking": False
    }
    try:
        response = requests.post(url, headers=headers, json=data, stream=True)
        full_text = ""
        for line in response.iter_lines():
            if line:
                decoded = line.decode('utf-8')
                if decoded.startswith('data: '):
                    try:
                        json_data = json.loads(decoded[6:])
                        if 'choices' in json_data:
                            full_text += json_data['choices'][0].get('delta', {}).get('content', '')
                    except: pass
        return full_text if full_text else "عذراً، لم أستطع الرد."
    except Exception as e:
        return "خطأ في الاتصال بالخادم."

# 5. منطق الإدخال
if prompt := st.chat_input("اسأل مساعد MRX..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🤖"):
        # الرد المخصص للمطور
        if "من صنعك" in prompt or "من مطورك" in prompt:
            response = "أنا مساعد MRX، تم تطويري بواسطة المبرمج: ماجد حاكم الدراك."
        else:
            response = get_ai_response(prompt)
        
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
