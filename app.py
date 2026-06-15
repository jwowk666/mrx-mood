from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# ضع منطق الـ API الخاص بك هنا
API_URL = "https://zailtqlrdcukgythlbwq.supabase.co/functions/v1/exos"
API_KEY = "exos_7d73425a42b9ebdbca982f04f84d0f267c2f720cf478a28c"

@app.route('/')
def index():
    return render_template('index.html') # هنا سيتم استدعاء ملف الـ HTML الخاص بك

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    # هنا يتم إرسال الطلب لـ API الخاص بك
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"}
    data = {"message": user_message, "model": "deepseek-ai/DeepSeek-V3.1", "stream": False}
    
    response = requests.post(API_URL, headers=headers, json=data)
    return jsonify({"reply": response.text})

if __name__ == '__main__':
    app.run(debug=True)
