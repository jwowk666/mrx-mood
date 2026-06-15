import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="MRX MOOD", page_icon="💀", layout="centered")

# CSS المخصص للهوية (الأسود، الأحمر، والأيقونات)
st.markdown("""
    <style>
    /* خلفية التطبيق سوداء بالكامل */
    .stApp {background-color: #000000; color: #ffffff;}
    
    /* صندوق الكتابة (الذي طلبت مثله) */
    .input-box {
        background-color: #1a1a1a;
        border: 2px solid #ff0000;
        border-radius: 20px;
        padding: 10px;
        color: white;
    }
    
    /* تنسيق الرسالة (التي طلبتها باللون الأحمر) */
    .mrx-message {
        background-color: #2b0000;
        border: 1px solid #ff0000;
        border-radius: 15px;
        padding: 15px;
        color: #ff4d4d; /* كلام MRX أحمر */
    }
    
    /* تنسيق أزرار الإجراءات (نسخ، قراءة) */
    .action-btn {
        background-color: #330000;
        color: #ff0000;
        border: 1px solid #ff0000;
        border-radius: 10px;
        padding: 5px 10px;
        margin-right: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. الجزء العلوي (صورة الجيميل في الدائرة الصفراء + شعار MRX في الدائرة الزرقاء)
col1, col2 = st.columns([1, 6])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/281/281769.png", width=50) # مكان صورة الجيميل
with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712120.png", width=50) # شعار MRX MOOD

# 2. منطقة عرض الإجابة (الخط الأحمر الكبير)
st.markdown("<hr style='border: 2px solid red;'>", unsafe_allow_html=True)
st.markdown("<div class='mrx-message'>هنا ستظهر إجابة MRX MOOD باللون الأحمر الفخم...</div>", unsafe_allow_html=True)

# 3. أزرار التحكم (نسخ + قراءة)
st.markdown("""
    <div style='margin-top: 10px;'>
        <button class='action-btn'>قراءة صوتية</button>
        <button class='action-btn'>نسخ الإجابة</button>
    </div>
""", unsafe_allow_html=True)

# 4. صندوق الكتابة (تحت)
st.markdown("<br><br>", unsafe_allow_html=True)
user_input = st.text_input("", placeholder="اسأل MRX MOOD أو ابدأ بكلمة 'تخيل' لتوليد...", label_visibility="collapsed")
