import streamlit as st
import pandas as pd
import altair as alt

# 앱 제목 설정
st.title('시계열 데이터 표시 및 Altair 그래프 그리기')

# 파일 업로더를 통한 데이터 업로드
uploaded_file = st.file_uploader("파일 업로드", type=['csv'])
if uploaded_file is not None:
    # 데이터를 DataFrame으로 읽기
    df = pd.read_csv(uploaded_file)
    
    # 테이블 형태로 데이터 표시
    st.write("### 업로드된 데이터", df)
    
    # Altair를 사용한 그래프 그리기
    st.write("### 시계열 그래프")
    c = alt.Chart(df).mark_line().encode(
        x='타임스탬프:T',  # 타임스탬프 컬럼의 데이터 형식이 datetime이라고 가정
        y='특성값:Q'      # 특성값 컬럼의 데이터 형식이 수량(quantitative)이라고 가정
    ).properties(
        width=800,
        height=400
    )
    
    st.altair_chart(c, use_container_width=True)
