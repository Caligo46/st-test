import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 앱 제목 설정
st.title('시계열 데이터 표시 및 그래프 그리기')

# 파일 업로더를 통한 데이터 업로드
uploaded_file = st.file_uploader("파일 업로드", type=['csv'])
if uploaded_file is not None:
    # 데이터를 DataFrame으로 읽기
    df = pd.read_csv(uploaded_file)

    # 테이블 형태로 데이터 표시
    st.write("### 업로드된 데이터", df)

    # 그래프 그리기 옵션
    if st.button('그래프 그리기'):
        st.write("### 시계열 그래프")

        # matplotlib를 이용한 그래프 그리기
        plt.figure(figsize=(10, 4))
        plt.plot(df.iloc[:, 0], df.iloc[:, 1], marker='o')
        plt.xticks(rotation=45)
        plt.xlabel('타임스탬프')
        plt.ylabel('특성값')
        plt.tight_layout()

        # Streamlit을 통해 그래프 표시
        st.pyplot(plt)