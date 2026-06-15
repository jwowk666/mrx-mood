# بدل كود requests.post القديم في app.py، استخدم هذا المنطق المدمج:
if prompt := st.chat_input("اسأل مساعد MRX..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        # 1. الاتصال المباشر (مثل السكربت الثاني)
        s = requests.Session()
        r = s.get("https://deep-seek.ai", headers={'User-Agent': 'Mozilla/5.0...'})
        c1 = s.cookies.get('XSRF-TOKEN')
        c2 = re.search(r'csrf-token["\s]+content=["\']([^"\']+)', r.text).group(1)
        
        # 2. إرسال الطلب
        res = s.post("https://deep-seek.ai/api/chat", headers={
            'X-CSRF-TOKEN': c2,
            'Cookie': f'XSRF-TOKEN={c1}',
            'Content-Type': 'application/json'
        }, json={
            "model": "deepseek/deepseek-v3.2",
            "messages": [{"role": "user", "content": prompt}]
        })
        
        # 3. عرض الرد
        answer = res.text 
        st.markdown(answer)
