def get_clean_response(user_input):
    """استخدام رابط chat-deep.ai المباشر (بدون الحاجة لمفتاح API)"""
    try:
        url = 'https://chat-deep.ai/wp-json/dsc/v1/chat'
        headers = {
            'Content-Type': 'application/json',
            'X-Wp-Nonce': '3c9123ed3a', # هذا هو المفتاح الذي يعمل معك
            'User-Agent': 'Mozilla/5.0'
        }
        payload = {
            "messages": [{"role": "user", "content": user_input}],
            "model": "deepseek-v4-flash",
            "thinking": False
        }
        
        response = requests.post(url, headers=headers, json=payload, stream=True)
        
        full_text = ""
        for line in response.iter_lines():
            if line:
                decoded = line.decode('utf-8')
                if decoded.startswith('data: '):
                    try:
                        data = json.loads(decoded[6:])
                        if 'choices' in data:
                            full_text += data['choices'][0].get('delta', {}).get('content', '')
                    except: continue
        return full_text if full_text else "عذراً، لم أستطع الحصول على رد."
    except Exception as e:
        return f"❌ خطأ تقني: {str(e)}"
