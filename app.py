import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="MRX MOOD", page_icon="⚡", layout="centered")

# تصميم CSS (التأثيرات الفخمة والنيون)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #000000, #0f0c29, #302b63);
        color: #ffffff;
    }
    .neon-title {
        text-align: center;
        color: #00d2ff;
        font-family: 'Arial Black', sans-serif;
        text-shadow: 0 0 15px #00d2ff;
    }
    .stButton>button {
        background: transparent;
        color: #00d2ff;
        border: 2px solid #00d2ff;
        border-radius: 50px;
        transition: 0.5s;
        width: 100%;
        font-weight: bold;
    }
    .stButton>button:hover {
        background: #00d2ff;
        color: black;
        box-shadow: 0 0 30px #00d2ff;
    }
    .card {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 20px;
        border: 1px solid #302b63;
    }
    </style>
    """, unsafe_allow_html=True)

# وضع الشعار في المنتصف
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712120.png", width=200)

# العنوان
st.markdown("<h1 class='neon-title'>MRX MOOD</h1>", unsafe_allow_html=True)

# منطقة العمل
st.markdown("<div class='card'>", unsafe_allow_html=True)
option = st.selectbox("اختر وضع التشغيل:", ["تحليل بصري", "تحليل صوتي", "دردشة ذكية"])
uploaded_file = st.file_uploader("📥 ارفع ملفك هنا", type=['png', 'jpg', 'mp3'])

if st.button("تفعيل MRX MOOD 🚀"):
    if uploaded_file:
        st.balloons()
        st.snow()
        st.success("تم تفعيل MRX MOOD بنجاح!")
        st.write(f"جاري معالجة: **{uploaded_file.name}**")
    else:
        st.warning("يرجى رفع ملف أولاً للبدء!")
st.markdown("</div>", unsafe_allow_html=True)
