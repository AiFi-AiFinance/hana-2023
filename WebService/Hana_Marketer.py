# app.py

import builtins
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


col1,empty2,col2 = st.columns([1, 0.03, 1])
with col1:
    image = Image.open('aifi.jpg')
    st.image(image, caption='Soyeon Seungyeon Sunghyun')
    
with col2:
    st.subheader("하나금융 파워온 프로젝트를 하면서...")
    st.markdown("[AiFi의 WiFi 블로그](https://blog.naver.com/annkwon11234)")
    st.markdown("[AiFi의 깃허브](https://github.com/AiFi-AiFinance)")

st.subheader("최종성과 발표 자료")
tab1, tab2, tab3 = st.tabs(["표지", "개발 동기", "서비스 소개"])

with tab1:
    st.header("표지")
    image1 = Image.open('001.png')
    st.image(image1)

with tab2:
    st.header("개발 동기")
    image2 = Image.open('002.png')
    st.image(image2) 

with tab3:
    st.header("서비스 소개")
    image3 = Image.open('003.png')
    st.image(image3)
