import streamlit as st
import requests
import json

# 🔐 Gemini API Key 입력
API_KEY = ""
API_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-pro:generateContent?key={API_KEY}"
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
            # 📌 응답 상태코드 확인
            print(f"Status Code: {response.status_code}")

            # 📌 여기가 바로 응답의 '원시 텍스트'
            print("Response Text (response.text):")
            print(response.text)
        if response.ok:
            try:
                response_json = response.json()  # ← JSON으로 파싱 시도
                st.success("✅ 유효한 JSON 응답입니다!")
                st.json(response_json)
            except ValueError:
                st.error("❌ JSON으로 변환할 수 없습니다. 응답 내용:")
                st.text(response.text)
            # response_json = response.json()
            # st.subheader("📦 전체 JSON 응답")
            # st.json(response_json)
            
            try:
                result = response_json['candidates'][0]['content']['parts'][0]['text']
                st.subheader("💬 Gemini의 응답")
                st.write(result)
            except (KeyError, IndexError):
                st.error("응답에서 텍스트를 추출할 수 없습니다.")
        else:
            st.error(f"API 오류 발생: {response.status_code}")
