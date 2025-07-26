import streamlit as st
import pandas as pd
import numpy as np

# 페이지 제목과 설명
st.title("🧡 단일 Streamlit 페이지 구성 요소 예시")
st.header("이 페이지는 Streamlit에서 활용 가능한 UI 요소를 한눈에 보여줍니다.")
st.subheader("모든 요소는 st.으로 시작해요!")

# -----------------------------
# 텍스트 출력
# -----------------------------
st.text("✅ 이것은 단순한 텍스트입니다.")
st.markdown("**이건 마크다운 형식으로 굵게!**")
st.code("print('Hello, world!')", language='python')  # 코드 블록

# -----------------------------
# 데이터프레임 및 표 출력
# -----------------------------
df = pd.DataFrame({
    '이름': ['서연', '지민', '현우'],
    '점수': [90, 85, 100]
})
st.dataframe(df)  # 정렬 가능 표
st.table(df)      # 정렬 불가능한 정적 표

# -----------------------------
# 내장 차트 출력
# -----------------------------
st.line_chart(df['점수'])  # 선 그래프
st.bar_chart(df['점수'])   # 막대 그래프
st.area_chart(df['점수'])  # 영역 그래프

# -----------------------------
# 이미지, 오디오, 비디오
# -----------------------------
st.image("https://placekitten.com/300/200", caption="고양이 이미지 예시")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")  # 오디오 삽입
st.video("https://www.youtube.com/watch?v=dlFA0Zq1k2A")  # 유튜브 영상 삽입

# -----------------------------
# 입력 요소들
# -----------------------------
name = st.text_input("이름을 입력하세요")  # 텍스트 입력
age = st.number_input("나이를 입력하세요", min_value=0, max_value=120, step=1)  # 숫자 입력
agree = st.checkbox("동의하시나요?")  # 체크박스
choice = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])  # 라디오 버튼
hobbies = st.multiselect("취미를 선택하세요", ["여행", "골프", "발레", "독서", "게임"])  # 다중 선택
color = st.selectbox("좋아하는 색은?", ["빨강", "초록", "파랑"])  # 드롭다운
st.date_input("날짜를 선택하세요")  # 날짜 입력
st.time_input("시간을 선택하세요")  # 시간 입력
uploaded_file = st.file_uploader("파일을 업로드하세요")  # 파일 업로드

# -----------------------------
# 슬라이더
# -----------------------------
level = st.slider("만족도를 선택하세요", 0, 100, 50)  # 슬라이더

# -----------------------------
# 버튼
# -----------------------------
if st.button("클릭하면 인사합니다"):
    st.success(f"안녕하세요, {name}님!")

# -----------------------------
# 진행바 및 스피너
# -----------------------------
st.progress(70)  # 진행 상태 바

with st.spinner("잠시만 기다려 주세요..."):  # 로딩 표시
    import time
    time.sleep(1)

# -----------------------------
# 메시지 출력
# -----------------------------
st.info("ℹ️ 참고사항을 알려드립니다.")
st.success("🎉 성공적으로 완료되었습니다!")
st.warning("⚠️ 주의가 필요합니다.")
st.error("❌ 오류가 발생했습니다.")

# -----------------------------
# 사이드바 사용
# -----------------------------
st.sidebar.title("사이드바 메뉴")
st.sidebar.text_input("사이드바 입력")

# -----------------------------
# 컬럼 나누기
# -----------------------------
col1, col2 = st.columns(2)
col1.write("왼쪽 컬럼입니다.")
col2.write("오른쪽 컬럼입니다.")

# -----------------------------
# 탭 사용
# -----------------------------
tab1, tab2 = st.tabs(["탭 1", "탭 2"])
with tab1:
    st.write("📁 첫 번째 탭 내용입니다.")
with tab2:
    st.write("📁 두 번째 탭 내용입니다.")

# -----------------------------
# 확장형 섹션 (expander)
# -----------------------------
with st.expander("클릭하면 펼쳐지는 내용"):
    st.write("📌 추가 정보를 여기에 넣을 수 있어요.")

# -----------------------------
# 상태 표시 (footer)
# -----------------------------
st.caption("© 2025 Seoyeon All rights reserved.")
