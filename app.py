import streamlit as st

# إعداد الصفحة
st.set_page_config(page_title="MRX MOOD", page_icon="⚡", layout="centered")

# إضافة تأثيرات CSS للفخامة (ألوان نيون)
st.markdown("""
    <style>
    .stApp {background: linear-gradient(135deg, #000000, #1a1a2e, #16213e); color: white;}
    h1 {color: #00d2ff; text-align: center; text-shadow: 0px 0px 20px #00d2ff;}
    .stButton>button {border: 2px solid #00d2ff; border-radius: 20px; color: #00d2ff; background: transparent;}
    .stButton>button:hover {background: #00d2ff; color: black;}
    </style>
    """, unsafe_allow_html=True)

st.title("⚡ MRX MOOD ⚡")
st.subheader("الذكاء الاصطناعي الأكثر فخامة")

# واجهة تفاعلية
with st.container():
    option = st.selectbox("اختر وضع المعالجة:", ["تحليل صور", "تحليل صوت", "دردشة عامة"])
    uploaded_file = st.file_uploader("ارفع ملفك هنا...", type=['png', 'jpg', 'mp3'])
    
    if st.button("تفعيل MRX MOOD"):
        st.balloons()  # مؤثرات بصرية عند الضغط
        st.success("جاري الاتصال بالنواة الذكية...")
        st.write(f"وضع التشغيل الحالي: {option}")

