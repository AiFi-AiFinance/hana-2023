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
col1,empty2,col2 = st.columns([1, 0.1, 8.9])

with col1:
    image_logo = Image.open('aifi_logo.png')
    st.image(image_logo)
    
with col2:
    st.title("하나뿐인 마케터 메인 페이지 입니다.👋\n")
    st.text("왼쪽에서 광고 신청 및 로그인 후 이용하실 수 있습니다.\n\n")
    
    
st.markdown("***")
st.write("이곳에 서비스 이용 방법과 서비스 설명에 대한 내용을 넣을 예정입니다..")
tab1, tab2 = st tabs(["서비스 소개", "서비스 이용 방법"])

with tab1:
    st.subheader("서비스 소개")

# 최종성과 발표 자료
st.markdown("***")
st.subheader("최종성과 발표 자료")
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["표지","발표 순서","기획 의도","서비스 명세","클라우드 SQL","전처리 전략","프론트엔드","인공지능"])

with tab1:
    st.subheader("표지")
    image1 = Image.open('001.png')
    st.image(image1)

with tab2:
    st.subheader("발표 순서")
    image2 = Image.open('002.png')
    st.image(image2) 

with tab3:
    st.subheader("기획 의도")
    image3 = Image.open('003.png')
    st.image(image3)
    
with tab4:
    st.subheader("서비스 명세")

with tab5:
    st.subheader("클라우드 SQL")
    
with tab6:
    st.subheader("전처리 전략")
    
with tab7:
    st.subheader("프론트엔드 (WEB, APP)")
    
with tab8:
    st.subheader("인공지능 (생성형AI, 머신러닝)")
    
# 기타 넣고 싶은거
st.markdown("***")
col1,empty2,col2 = st.columns([1, 0.03, 1])

with col1:
    image = Image.open('aifi.jpg')
    st.image(image, caption='Soyeon Seungyeon Sunghyun')
    
with col2:
    st.subheader("하나금융 파워온 프로젝트를 하면서...")
    st.markdown("블로그에 글도 쓰고, [AiFi의 WiFi 블로그](https://blog.naver.com/annkwon11234)")
    st.markdown("깃허브에 코드 올리고, [AiFi의 깃허브](https://github.com/AiFi-AiFinance)")
    st.title("즐거웠습니다.")
    
