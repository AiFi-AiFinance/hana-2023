# app.py

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from time import sleep


# 페이지 기본 설정
st.set_page_config(
    page_icon="🐶",
    page_title="하나뿐인 마케터",
    layout="wide"
)

# 로딩바 구현하기
with st.spinner(text="페이지 로딩중..."):
    sleep(2)

# 페이지 헤더, 서브헤더 제목 설정
st.header("하나뿐인 마케터 메인페이지입니다.👋")
st.subheader("\n좌측에서 광고 신청 및 로그인 후 이용하실 수 있습니다.\n")

# 이미지 추가
# img_url = 'https://github.com/AiFi-AiFinance/hana-2023/blob/main/WebService/phoenix.png'
# st.image(img_url, caption='Soyeon Seungyeon Sunghyun')

# image = Image.open('images/001.png', 'rb')
# st.image(image, caption='ppt001')

image = Image.open('./images/001.png')
st.image(image, caption='ppt001')

# 페이지 컬럼 분할(예: 부트스트랩 컬럼, 그리드)
# cols = st.columns((1, 1, 2))
# cols[0].metric("10/11", "15 °C", "2")
# cols[0].metric("10/12", "17 °C", "2 °F")
# cols[0].metric("10/13", "15 °C", "2")
# cols[1].metric("10/14", "17 °C", "2 °F")
# cols[1].metric("10/15", "14 °C", "-3 °F")
# cols[1].metric("10/16", "13 °C", "-1 °F")

# 라인 그래프 데이터 생성(with. Pandas)
# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])

# 컬럼 나머지 부분에 라인차트 생성
# cols[2].line_chart(chart_data)