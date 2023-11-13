# pages/2_Report.py

# 데이터 베이스에서 store_name이 승연이네랑 일치하는 데이터의 passwd를 반환, 아니면 -1 
# from Database import get_pw
def get_pw(store_name):
    if store_name == '승연이네':
        return '1234'
    else:
        return -1
    
# ------------------------ database ------------------------ #
# 광고 테이블에서 머신러닝 결과랑 챗gpt 결과 받아오기
# from Database import get_ad_type, get_gpt_ments
def get_ad_type(store_code):
    if store_code == '1':
        return '쇼핑/유통'
    else:
        return -1
def get_gpt_ments(store_code):
    if store_code == '1':
        return ["겨울을 더욱 스타일리시하게! 모자 가게에서 트렌디한 모자를 만나보세요.",
                "패션에는 세부사항이 중요합니다. 모자 가게에서 다양한 스타일의 모자를 찾아보세요.",
                "모자 가게에서는 겨울에 딱 맞는 따뜻하고 멋진 모자를 만나실 수 있습니다. 지금 바로 방문해보세요!"]
    else:
        return -1
    
# 선택한 gpt ment를 광고 테이블에 저장하기
# from Database import input_option
def input_option(str_ment):
    return str_ment
    
# ------------------------ streamlit ------------------------ #
import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError

# 페이지 기본 설정
st.set_page_config(
    page_icon="⭐️",
    page_title="하나뿐인 마케터",
    layout="wide",
)

# 사이드바 로그인
st.sidebar.header("로그인")
st.sidebar.markdown("### 기업 정보를 입력해주세요.")
store_name = st.sidebar.text_input('업체명을 입력해주세요.', value="")
passwd = st.sidebar.text_input('비밀번호를 입력해주세요.', value="", type='password')
if st.sidebar.button("입력"):
    if get_pw(store_name) != passwd:
        # 로그인 성공
        st.subheader("하나뿐인 마케터에서 분석한 패용입니다.")
        st.text(get_ad_type('1'))
        ment = st.radio("gpt가 추천하는 멘트 세가지 중 하나를 골라주세요.", options=get_gpt_ments('1'))
        st.text(input_option(ment))
    else:
        # 로그인 실패
        st.error("비밀번호를 확인해주세요.")