import streamlit as st
from pyvis.network import Network
import networkx as nx

# Streamlit 앱 제목
st.title("Graph Visualization with Streamlit and Pyvis")

# 노드와 엣지를 입력받기 위한 폼
st.sidebar.header("Graph Input")
nodes_input = st.sidebar.text_area("Enter nodes (comma separated):", "A,B,C,D")
edges_input = st.sidebar.text_area("Enter edges (comma separated, format: node1-node2):", "A-B,B-C,C-D,D-A")

# 노드와 엣지 입력값 파싱
nodes = [node.strip() for node in nodes_input.split(",")]
edges = [tuple(edge.strip().split("-")) for edge in edges_input.split(",")]

# Pyvis 네트워크 생성
net = Network(height="750px", width="100%", notebook=True)

# 노드 추가
for node in nodes:
    net.add_node(node, label=node)

# 엣지 추가
for edge in edges:
    net.add_edge(*edge)

# 네트워크 렌더링
net.show("graph.html")

# Streamlit에 Pyvis 네트워크 렌더링
st.write("### Graph Visualization")
st.components.v1.html(open("graph.html", 'r').read(), height=800)

# 네트워크 정보 출력
st.write("### Network Information")
st.write(f"**Nodes:** {', '.join(nodes)}")
st.write(f"**Edges:** {', '.join([f'{e[0]}-{e[1]}' for e in edges])}")


# import streamlit as st
# import pandas as pd
# import altair as alt
# import seaborn as sns
# import matplotlib.pyplot as plt

# # 앱 제목 설정
# st.title('CSV 파일 데이터 시각화')

# # 더미 데이터 생성
# dummy_data = {
#     'D+': [5, 15, 25, 40, 53, 63, 72, 99, 112],
#     'NPS': [13, 53, 50, 43, 46, 43, 50, 55, 55],
#     # 추가적인 더미 데이터 특성
#     'Satisfaction': [3, 7, 6, 5, 8, 7, 9, 8, 7],
#     'Engagement': [4, 9, 6, 8, 7, 5, 7, 8, 8]
# }
# df_dummy = pd.DataFrame(dummy_data)

# # 파일 업로더 생성
# uploaded_file = st.file_uploader("CSV 파일을 선택해주세요", type=['csv'])

# # 예제 데이터 보기 버튼
# if st.button('예제'):
#     df = df_dummy
# else:
#     if uploaded_file is not None:
#         # 데이터를 DataFrame으로 읽기
#         df = pd.read_csv(uploaded_file)
#     else:
#         # 업로드된 파일이 없으면 더미 데이터 사용
#         df = df_dummy

# # Pairplot 그리기 버튼
# if st.button('Pairplot 그리기'):
#     # Seaborn으로 pairplot 그리기
#     st.write("### Pairplot")
#     sns.pairplot(df)
#     st.pyplot(plt)

# # 데이터의 헤더에서 선택 가능한 옵션 생성
# column_names = df.columns.tolist()

# # x축과 y축을 위한 헤더 선택
# x_axis = st.selectbox("X 축을 선택하세요", column_names, index=0)
# y_axis = st.selectbox("Y 축을 선택하세요", column_names, index=1 if len(column_names) > 1 else 0)

# # Altair를 이용한 그래프 그리기
# chart = alt.Chart(df).mark_line().encode(
#     x=x_axis,
#     y=y_axis,
#     tooltip=[x_axis, y_axis]
# ).interactive().properties(
#     width=800,
#     height=400
# )

# st.altair_chart(chart, use_container_width=True)
