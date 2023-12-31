# app.py

import builtins
import streamlit as st
# import streamlit_authenticator as stauth

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

# 로딩바
with st.spinner(text="페이지 로딩중..."):
    sleep(2)
    
# 사이드바 로그인
# 데이터 베이스에서 store_name이 승연이네랑 일치하는 데이터의 passwd를 반환, 아니면 -1 
# from Database import get_pw
def get_pw(store_name):
    if store_name == '승연이네':
        return '1234'
    else:
        return -1

st.sidebar.header("로그인")
st.sidebar.markdown("### 기업 정보를 입력해주세요.")
store_name = st.sidebar.text_input('업체명을 입력해주세요.', value="")
passwd = st.sidebar.text_input('비밀번호를 입력해주세요.', value="", type='password')
if st.sidebar.button("입력"):
    if passwd != None and get_pw(store_name) == passwd:
        # 로그인 성공
        image = Image.open('aifi.jpg')
        st.sidebar.image(image, caption='Soyeon Seungyeon Sunghyun')
        st.sidebar.success(f"{store_name} 환영합니다.") 
    else:
        # 로그인 실패
        st.sidebar.error("비밀번호를 확인해주세요.")

# 페이지 헤더, 서브헤더 제목 설정
col1,empty2,col2 = st.columns([1, 0.1, 8.9])

with col1:
    image_logo = Image.open('aifi_logo.png')
    st.image(image_logo, width=100)
    
with col2:
    st.title("하나뿐인 마케터 메인 페이지 입니다.👋\n")
    st.text("왼쪽에서 광고 신청 및 로그인 후 이용하실 수 있습니다.\n\n")
    
st.markdown("***")
tab1, tab2 = st.tabs(['서비스 소개', '서비스 이용 방법'])
with tab1:
    st.write('⠀고객 맞춤형 광고를 경험해 보세요. 불필요한 광고와 상품 추천은 고객에게 부정적인 인상을 줄 수 있습니다. 하나뿐인 마케터는 고객 데이터를 기반으로 개인에게 맞춤형 광고를 제공하여 위와 같은 부정적인 인상을 최소화합니다.')
    st.write('⠀광고 문구에 대해 걱정하실 필요 없습니다. 하나뿐인 마케터를 통해 생성형 AI를 이용한 광고 문구 추천 서비스를 받으실 수 있습니다. 또한 하나뿐인 마케터에서는 타겟층 정보 분석 및 광고 스타일 제안 등 클릭 건수를 기반으로 도출된 자료를 받으실 수 있습니다.')

with tab2:
    col1,empty2,col2,empty2,col3 = st.columns([1, 0.1, 1, 0.1, 1])
with tab2, col1:
    image_apply = Image.open('광고신청페이지_Edited.png')
    st.image(image_apply)
    st.write('①좌측 상단 Apply 선택')
    st.write('②기업 정보 및 광고 정보 입력')
with tab2, col2:
    image_report = Image.open('광고문구추천_Edited.png')
    st.image(image_report)
    st.write('①좌측 상단 Report 선택')
    st.write('②좌측 하단 로그인')
    st.write('③추천 광고 문구 선택')
with tab2, col3:
    image_extention = Image.open('광고연장신청_Edited.png')
    st.image(image_extention)
    st.write('①좌측 상단 Extention 선택')
    st.write('②광고 연장 기간 입력')
    
   

# 최종성과 발표 자료
# st.markdown("***")
# st.subheader("최종성과 발표 자료")
# tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["표지","발표 순서","기획 의도","서비스 명세","클라우드 SQL","전처리 전략","프론트엔드","인공지능"])

# with tab1:
#     st.subheader("표지")
#     image1 = Image.open('001.png')
#     st.image(image1)

# with tab2:
#     st.subheader("발표 순서")
#     image2 = Image.open('002.png')
#     st.image(image2) 

# with tab3:
#     st.subheader("기획 의도")
#     image3 = Image.open('003.png')
#     st.image(image3)
    
# with tab4:
#     st.subheader("서비스 명세")

# with tab5:
#     st.subheader("클라우드 SQL")
    
# with tab6:
#     st.subheader("전처리 전략")
    
# with tab7:
#     st.subheader("프론트엔드 (WEB, APP)")
    
# with tab8:
#     st.subheader("인공지능 (생성형AI, 머신러닝)")
    
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
    
