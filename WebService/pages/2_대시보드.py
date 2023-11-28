# pages/2_Report.py


    
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
from PIL import Image
from urllib.error import URLError

# 페이지 기본 설정
st.set_page_config(
    page_icon="⭐️",
    page_title="하나뿐인 마케터",
    layout="wide",
)

st.subheader("하나뿐인 마케터에서 분석한 내용입니다.")
st.text("왼쪽에서 로그인 후 이용하실 수 있습니다.")
st.markdown("***")
        

        
# 페이지

with st.expander("겨울 모자 광고"):
    st.text(get_ad_type('1'))
    ment = st.radio("gpt가 추천하는 멘트 세가지 중 하나를 골라주세요.", options=get_gpt_ments('1'))
    input_option(ment)
    st.write(" 겨울 모자 광고의 주요 고객 층은 20대 여성입니다. MZ 세대가 겨울 패션 아이템을 선호합니다. ")
    
with st.expander("수정과 광고"):
    st.text(get_ad_type('1'))
    ment = st.radio("gpt가 추천하는 멘트 세가지 중 하나를 골라주세요.", options=get_gpt_ments('1'))
    input_option(ment)