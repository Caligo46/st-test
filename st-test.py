import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# 앱 제목 설정
st.title('아아 테스트중입니다 /n 시계열 데이터 수정 가능한 테이블과 그래프')

# 데이터 생성 함수
def generate_data(num_points):
    time_stamps = pd.date_range('today', periods=num_points, freq='T')
    values = np.random.randn(num_points).cumsum()  # 누적 합계를 가지는 랜덤 값
    return pd.DataFrame({'Time Stamp': time_stamps, 'Value': values})

# 사용자 입력을 받아 데이터 포인트의 수 설정
num_points = st.sidebar.slider('데이터 포인트 수', min_value=10, max_value=100, value=50)
df = generate_data(num_points)

# 데이터프레임을 세션 상태에 저장하여 수정 사항 유지
if 'dataframe' not in st.session_state:
    st.session_state.dataframe = df

# 데이터프레임 수정을 위한 인덱스와 값 입력
index_to_edit = st.number_input('수정할 데이터 포인트의 인덱스 입력', min_value=0, max_value=len(df)-1, value=0, step=1)
new_value = st.number_input('새로운 값 입력', value=float(st.session_state.dataframe.iloc[index_to_edit]['Value']))

# 데이터 업데이트 버튼
if st.button('업데이트'):
    st.session_state.dataframe.iloc[index_to_edit, st.session_state.dataframe.columns.get_loc('Value')] = new_value
    st.success('데이터 업데이트 완료!')

# 수정된 데이터프레임 표시
st.write("### 수정된 데이터", st.session_state.dataframe)

# Altair를 이용한 시각화
chart = alt.Chart(st.session_state.dataframe).mark_line().encode(
    x='Time Stamp:T',
    y='Value:Q',
    tooltip=['Time Stamp:T', 'Value:Q']
).interactive().properties(
    width=800,
    height=400
)

st.altair_chart(chart, use_container_width=True)
