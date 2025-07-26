import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. 지도 기반 위치 시각화 예시
st.header("1. 지도 기반 위치 시각화 예시")
# 임의의 위도, 경도 데이터 생성
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.5665, 126.9780],  # 서울 중심 좌표 근처
    columns=['lat', 'lon']
)
st.map(map_data)  # 지도에 데이터 표시

# 2. CSV 파일 업로드 및 시각화 예시
st.header("2. CSV 파일 업로드 및 시각화 예시")
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요.", type=["csv"])
if uploaded_file is not None:
    # 업로드된 파일을 데이터프레임으로 읽기
    df = pd.read_csv(uploaded_file)
    st.write("업로드된 데이터 미리보기:")
    st.dataframe(df)  # 데이터 표로 보여주기

    # 수치형 컬럼만 선택하여 차트로 시각화
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    if numeric_cols:
        st.line_chart(df[numeric_cols])
    else:
        st.info("시각화할 수치형 컬럼이 없습니다.")

# 3. 난수 스트리밍을 시뮬레이션한 실시간 라인 차트
st.header("3. 난수 스트리밍을 시뮬레이션한 실시간 라인 차트")
chart_placeholder = st.empty()  # 차트가 표시될 자리

# 초기 데이터프레임 생성
stream_df = pd.DataFrame(np.random.randn(1, 1), columns=["Random Value"])

# 20번 반복하며 실시간으로 데이터 추가 및 차트 업데이트
for i in range(20):
    new_row = pd.DataFrame(np.random.randn(1, 1), columns=["Random Value"])
    stream_df = pd.concat([stream_df, new_row], ignore_index=True)
    chart_placeholder.line_chart(stream_df)
    time.sleep(0.2)  # 0.2초 대기(실시간 효과)


import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

st.header("4. matplotlib 한글 그래프 예시")

# 프로젝트 내 폰트 경로
font_path = os.path.join("fonts", "NanumGothic-Regular.ttf")

if os.path.exists(font_path):
    fontprop = fm.FontProperties(fname=font_path, size=14)
    plt.rcParams['axes.unicode_minus'] = False  # 마이너스 깨짐 방지

    # 예시 데이터
    data = [30, 20, 50]
    labels = ['사과', '바나나', '포도']

    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(data, labels=labels, autopct='%1.1f%%', textprops={'fontproperties': fontprop})
    ax.set_title("과일 선호도 (예시)", fontproperties=fontprop)

    # 레이블에도 폰트 적용
    for text in texts + autotexts:
        text.set_fontproperties(fontprop)

    st.pyplot(fig)
else:
    st.warning("폰트 파일을 찾을 수 없습니다. fonts 폴더 안에 NanumGothic-Regular.ttf가 있는지 확인하세요.")
