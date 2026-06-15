import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="MRX MOOD", page_icon="💀", layout="centered")

# CSS المحدث (كل شيء أسود وأحمر فخم)
st.markdown("""
    <style>
    .stApp {background-color: #000000;}
    
    /* تنسيق مربع الكتابة */
    .stTextInput > div > div > input {
        background-color: #1a1a1a !important;
        color: white !important;
        border: 2px solid #ff0000 !important;
        border-radius: 20px !important;
        padding: 15px !important;
    }
    
    /* زر الإرسال الفخم */
    div.stButton > button {
        background-color: #ff0000 !important;
        color: white !important;
        border-radius: 50% !important;
        width: 50px !important;
        height: 50px !important;
        border: none !important;
        font-size: 20px !important;
    }
    
    .mrx-text {color: #ff0000; font-weight: bold;}
    </style>
    """, unsafe_allow_html=True)

# الجزء العلوي
col1, col2 = st.columns([1, 10])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/281/281769.png", width=40) # دائرة الشخص
with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712120.png", width=40) # شعار MRX

# منطقة الرد (تظهر بلون أحمر)
st.markdown("<p class='mrx-text'>MRX MOOD: جاهز للسيطرة...</p>", unsafe_allow_html=True)

# منطقة الكتابة (مربع + زر إرسال بجانبه)
c1, c2 = st.columns([9, 1])
with c1:
    user_input = st.text_input("", placeholder="اسأل MRX MOOD أو ابدأ بكلمة 'تخيل'...")
with c2:
    send_btn = st.button("⬆") # هذا هو زر الإرسال

if send_btn:
    st.write(f"أنت كتبت: {user_input}") # هنا ستظهر إجابة الذكاء الاصطناعي لاحقاً
