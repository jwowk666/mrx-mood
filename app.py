import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="مساعد MRX", layout="wide")

# تصميم CSS ليكون مطابقاً للصورة تماماً (مربع أسود سفلي)
st.markdown("""
    <style>
    .stApp {background-color: #000000;}
    
    /* الحاوية السفلية (المربع الأسود) */
    .chat-container {
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        width: 80%;
        background-color: #1a1a1a;
        border-radius: 25px;
        padding: 15px;
        border: 1px solid #333;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    /* تنسيق مربع الكتابة */
    .stTextInput > div > div > input {
        background-color: transparent !important;
        color: white !important;
        border: none !important;
    }
    
    /* زر الإرسال الدائري */
    .send-btn {
        background-color: #333 !important;
        border-radius: 50% !important;
        color: white !important;
    }
    
    .title-text {
        text-align: center;
        color: #ff0000;
        font-family: sans-serif;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# العنوان
st.markdown("<h2 class='title-text'>مساعد MRX</h2>", unsafe_allow_html=True)

# الحاوية السفلية (المربع الأسود المطابق للصورة)
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

# محتويات المربع السفلي
col1, col2, col3, col4, col5 = st.columns([0.5, 8, 1, 1, 1])

with col1:
    st.button("➕") # زر الإضافة
with col2:
    user_input = st.text_input("", placeholder="اسأل مساعد MRX أو ابدأ بكلمة 'تخيل' لتوليد...", label_visibility="collapsed")
with col3:
    st.button("⬆") # زر الإرسال
with col4:
    st.button("🎙️") # زر الصوت
with col5:
    st.button("🖼️") # زر الصور

st.markdown("</div>", unsafe_allow_html=True)
