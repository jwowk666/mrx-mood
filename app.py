import streamlit as st
import requests
import json

# إعداد الصفحة وتصميم الألوان
st.set_page_config(page_title="MRX MOOD", page_icon="🤖")

st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; }
    /* لون رسائل المستخدم */
    div[data-testid="stChatMessage"][data-author="user"] { background-color: #8b0000 !important; color: white !important; }
    /* لون رسائل المساعد */
    div[data-testid="stChatMessage"][data-author="assistant"] { background-color: #ffffff !important; color: black !important; }
    /* شكل صندوق الكود */
    pre { background-color: #1c1c1c !important; color: #ffffff !important; border: 1px solid #ff0000 !important; }
    </style>
""", unsafe_allow_html=True)

st.title("MRX MOOD 🤖")

if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة
for msg in st.session_state.messages:
    avatar = "👤" if msg["role"] == "user" else "🤖"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

# دالة الاتصال بالـ API (المحرك الذي يجعل المساعد يتكلم)
def get_ai_response(user_input):
    try:
        # استخدام الـ API الذي زودتني به
        response = requests.post(
            'https://chat-deep.ai/wp-json/dsc/v1/chat',
            headers={'Content-Type': 'application/json', 'X-Wp-Nonce': '3c9123ed3a'},
            json={"messages": [{"role": "user", "content": user_input}], "model": "deepseek-v4-flash", "thinking": False},
            stream=True
        )
        full_response = ""
        for line in response.iter_lines():
            if line:
                data_str = line.decode('utf-8')
                if data_str.startswith('data: '):
                    try:
                        data = json.loads(data_str[6:])
                        if 'choices' in data:
                            full_response += data['choices'][0].get('delta', {}).get('content', '')
                    except: pass
        return full_response
    except:
        return "عذراً، لم أستطع الاتصال بالخادم الآن."

# منطقة الإدخال
if prompt := st.chat_input("اسأل مساعد MRX..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("MRX يكتب..."):
            # منطق الرد: إذا سأل عن المطور يرد، وإلا يرسل السؤال للـ API
            if "من صنعك" in prompt:
                response = "تم تطويري بواسطة ماجد حاكم الدراك."
            else:
                response = get_ai_response(prompt)
            
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
