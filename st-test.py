import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# 앱 제목 설정
st.title('아아 테스트중입니다 \n 시계열 데이터와 Altair 그래프')

# 데이터 생성
def generate_data(num_points):
    # 현재 날짜와 시간을 기준으로 타임스탬프 생성
    time_stamps = pd.date_range('today', periods=num_points, freq='T')
    values = np.random.randn(num_points).cumsum()  # 누적 합계를 가지는 랜덤 값
    return pd.DataFrame({'Time Stamp': time_stamps, 'Value': values})

# 사용자 입력을 받아 데이터 포인트의 수 설정
num_points = st.slider('데이터 포인트 수', min_value=10, max_value=100, value=50)
df = generate_data(num_points)

# 데이터프레임을 테이블로 표시
st.write("### 생성된 데이터", df)

# Altair를 이용한 시각화
chart = alt.Chart(df).mark_line().encode(
    x='Time Stamp:T',
    y='Value:Q',
    tooltip=['Time Stamp:T', 'Value:Q']
).interactive().properties(
    width=800,
    height=400
)

st.altair_chart(chart, use_container_width=True)
