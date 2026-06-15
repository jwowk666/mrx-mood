import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="MRX MOOD", page_icon="🤖")

# CSS فخم ومحمي
st.markdown("""
    <style>
    .stApp { background-color: #000; color: #fff; }
    </style>
""", unsafe_allow_html=True)

st.title("MRX MOOD 🤖")

if "messages" not in st.session_state:
    st.session_state.messages = []

# عرض المحادثة
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# منطقة الإدخال
if prompt := st.chat_input("اسأل مساعد MRX..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # الرد على سؤال المطور
        if "من صنعك" in prompt or "من مطورك" in prompt:
            response = "أنا مساعد MRX، تم تطويري بواسطة المبرمج: ماجد حاكم الدراك."
        
        # الرد الافتراضي (مثال على كيفية كتابة الكود لكي يظهر زر النسخ)
        else:
            response = '''إليك كود بايثون احترافي:
```python
def hello_mrx():
    print("Welcome to MRX MOOD")
```'''
        
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
