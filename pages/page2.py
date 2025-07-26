import streamlit as st
import pandas as pd

# 1. CSV 파일 업로드 기능
st.header("성적 데이터 업로드 및 분석")

# 파일 업로더 위젯 생성 (csv 파일만 허용)
uploaded_file = st.file_uploader("학생 성적 CSV 파일을 업로드하세요.", type=["csv"])

if uploaded_file is not None:
    # CSV 파일을 데이터프레임으로 읽기
    df = pd.read_csv(uploaded_file)
    
    # 데이터 미리보기 표시
    st.subheader("업로드된 데이터 미리보기")
    st.dataframe(df)
    
    # 학생별 평균 점수 계산
    score_cols = ['수학', '영어', '과학']  # 컬럼명 수정
    if all(col in df.columns for col in score_cols):
        df['평균 점수'] = df[score_cols].mean(axis=1)
        
        st.subheader("학생별 평균 점수")
        st.dataframe(df[['이름', '평균 점수']])  # 컬럼명 수정
        
        # 과목별 석차 계산 및 표시
        st.subheader("과목별 석차")
        rank_df = df[['이름']].copy()  # 컬럼명 수정
        for col in score_cols:
            # 내림차순(높은 점수가 1등)
            rank_df[f'{col} 석차'] = df[col].rank(ascending=False, method='min').astype(int)
        st.dataframe(pd.concat([df[['이름']], rank_df.iloc[:, 1:]], axis=1))
        
        # 평균 점수 기준 전체 석차
        st.subheader("평균 점수 기준 전체 석차")
        df['평균 석차'] = df['평균 점수'].rank(ascending=False, method='min').astype(int)
        st.dataframe(df[['이름', '평균 점수', '평균 석차']].sort_values('평균 석차'))
        
        # 시각화: 학생별 평균 점수 바 차트
        st.subheader("학생별 평균 점수(Bar Chart)")
        st.bar_chart(df.set_index('이름')['평균 점수'])
    else:
        st.error("필수 컬럼(이름, 수학, 영어, 과학)이 모두 포함되어야 합니다.")
else:
    st.info("학생 성적 CSV 파일을 업로드하여 주십시오.")