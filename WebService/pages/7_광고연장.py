# 고객 분석 로그인한 기업이 가진 광고의 고객 분석

# 페이지 기본 설정
import streamlit as st
# from st_pages import hide_pages
from PIL import Image
st.set_page_config(page_title="광고하마 고객분석",page_icon="🦛",layout="wide")
# hide_pages(["회원가입","광고연장"])
st.subheader("광고하마가 분석한 우리 매장의 고객입니다.")
st.text("현재 광고는 아이러브커피 매장의 수정과입니다.")
st.markdown("***")

# 사이드바
with st.sidebar:
    st.text("아이러브커피")
    image002 = Image.open('002.png')
    st.image(image002)