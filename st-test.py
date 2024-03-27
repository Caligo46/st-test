import streamlit as st
import pandas as pd
import altair as alt

# 앱 제목 설정
st.title('CSV 파일 데이터 시각화')

# 파일 업로더 생성
uploaded_file = st.file_uploader("CSV 파일을 선택해주세요", type=['csv'])

if uploaded_file is not None:
    # 데이터를 DataFrame으로 읽기
    df = pd.read_csv(uploaded_file)
    
    # 업로드된 데이터의 헤더 표시
    st.write("### 데이터 미리보기", df.head())
    
    # 데이터의 헤더에서 선택 가능한 옵션 생성
    column_names = df.columns.tolist()
    
    # x축과 y축을 위한 헤더 선택
    x_axis = st.selectbox("X 축을 선택하세요", column_names, index=0)
    y_axis = st.selectbox("Y 축을 선택하세요", column_names, index=1 if len(column_names) > 1 else 0)
    
    # Altair를 이용한 그래프 그리기
    chart = alt.Chart(df).mark_line().encode(
        x=x_axis,
        y=y_axis,
        tooltip=[x_axis, y_axis]
    ).interactive().properties(
        width=800,
        height=400
    )
    
    st.altair_chart(chart, use_container_width=True)
