import streamlit as st
import requests
import json

# 🔐 Gemini API Key 입력
API_KEY = "YOUR_GEMINI_API_KEY"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"

# 앱 UI
st.title("🧠 Gemini와 대화하기")
prompt = st.text_area("질문을 입력하세요", height=150)

if st.button("Gemini에게 질문하기"):
    if not API_KEY or API_KEY == "YOUR_GEMINI_API_KEY":
        st.error("API 키를 설정해주세요.")
    elif not prompt.strip():
        st.warning("질문을 입력해주세요.")
    else:
        headers = {"Content-Type": "application/json"}
        data = {
            "contents": [
                {
                    "parts": [{"text": prompt}]
                }
            ]
        }

        with st.spinner("Gemini가 응답 중입니다..."):
            response = requests.post(API_URL, headers=headers, json=data)

        if response.ok:
            response_json = response.json()
            st.subheader("📦 전체 JSON 응답")
            st.json(response_json)

            try:
                result = response_json['candidates'][0]['content']['parts'][0]['text']
                st.subheader("💬 Gemini의 응답")
                st.write(result)
            except (KeyError, IndexError):
                st.error("응답에서 텍스트를 추출할 수 없습니다.")
        else:
            st.error(f"API 오류 발생: {response.status_code}")
