# 대시보드: 로그인한 기업의 광고 리스트 보여주기

# 페이지 기본 설정
import streamlit as st
# from st_pages import hide_pages
st.set_page_config(page_title="광고하마 대시보드",page_icon="🦛",layout="wide")
# hide_pages(["회원가입","광고연장"])
st.subheader("하나뿐인 마케터에 신청한 광고입니다.")
st.text("현재 로그인 된 매장은 아이러브커피입니다.")
st.markdown("***")

# 사이드바
with st.sidebar:
  st.text("아이러브커피")
  
# 페이지 내용 
import pandas as pd
import pydeck as pdk
from PIL import Image
from urllib.error import URLError
import numpy as np

# kpi 1 

kpi1, kpi2, kpi3 = st.columns(3)

with kpi1:
    st.markdown("**First KPI**")
    number1 = 111 
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number1}</h1>", unsafe_allow_html=True)

with kpi2:
    st.markdown("**Second KPI**")
    number2 = 222 
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number2}</h1>", unsafe_allow_html=True)

with kpi3:
    st.markdown("**Third KPI**")
    number3 = 333 
    st.markdown(f"<h1 style='text-align: center; color: red;'>{number3}</h1>", unsafe_allow_html=True)

st.markdown("<hr/>",unsafe_allow_html=True)


# kpi 1 

kpi01, kpi02, kpi03, kpi04, kpi05 = st.columns(5)

with kpi01:
    st.markdown("**Another 1st KPI**")
    number1 = 111 
    st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)

with kpi02:
    st.markdown("**Another 1st KPI**")
    number1 = 222 
    st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)

with kpi03:
    st.markdown("**Another 1st KPI**")
    number1 = 555 
    st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)

with kpi04:
    st.markdown("**Another 1st KPI**")
    number1 = 333 
    st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)

with kpi05:
    st.markdown("**Another 1st KPI**")
    number1 = 444 
    st.markdown(f"<h1 style='text-align: center; color: yellow;'>{number1}</h1>", unsafe_allow_html=True)

st.markdown("<hr/>",unsafe_allow_html=True)


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["광고하마", "광곰", "광아지"])
st.line_chart(chart_data)
        
# 페이지
col1,col2,col3 = st.columns(3)
with col1:
    with st.expander("겨울 모자 광고"):
        st.write("겨울 모자 광고")
        st.bar_chart(chart_data)

with col2:  
    with st.expander("수정과 광고"):
        st.write("겨울 모자 광고")
        st.line_chart(chart_data) 
        
with col3:  
    with st.expander("수과 광고"):
        st.write("겨울 모자 광고")
        st.line_chart(chart_data) 