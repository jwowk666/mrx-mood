import streamlit as st
import requests
import json

st.set_page_config(page_title="MRX MOOD", page_icon="🤖")

st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; }
    </style>
""", unsafe_allow_html=True)

st.title("MRX MOOD 🤖")

# إدارة المحادثة في الذاكرة
if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض الرسائل السابقة
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# الدالة الخاصة بك (تم دمجها هنا)
def send_message_to_api(messages):
    try:
        response = requests.post(
            'https://chat-deep.ai/wp-json/dsc/v1/chat',
            headers={
                'Content-Type': 'application/json',
                'X-Wp-Nonce': '3c9123ed3a', # مفتاحك السري
                'User-Agent': 'Mozilla/5.0'
            },
            json={
                "messages": messages,
                "model": "deepseek-v4-flash",
                "thinking": False
            },
            stream=True
        )
        
        full_response = ""
        for line in response.iter_lines():
            if line:
                line_str = line.decode('utf-8')
                if line_str.startswith('data: '):
                    data_str = line_str[6:]
                    try:
                        data = json.loads(data_str)
                        if 'choices' in data:
                            content = data['choices'][0].get('delta', {}).get('content', '')
                            full_response += content
                    except: pass
        return full_response
    except Exception as e:
        return f"خطأ في الاتصال: {str(e)}"

# حقل الإدخال
if prompt := st.chat_input("اسأل مساعد MRX..."):
    # إضافة رسالة المستخدم للتاريخ
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # الحصول على الرد من الـ API
    with st.chat_message("assistant"):
        # رد مخصص للمطور
        if "من صنعك" in prompt or "من مطورك" in prompt:
            response = "أنا مساعد MRX، تم تطويري بواسطة المبرمج: ماجد حاكم الدراك."
        else:
            response = send_message_to_api(st.session_state.messages)
        
        # عرض الرد (الـ Markdown سيتعرف على الأكواد ويضيف زر النسخ تلقائياً)
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
