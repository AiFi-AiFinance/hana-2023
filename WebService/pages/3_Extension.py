# pages/2_Chart_Demo.py

import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError
from dateutil import parser


# 페이지 기본 설정
st.set_page_config(
    page_icon="🐶",
    page_title="하나뿐인 마케터",
    layout="wide",
)

#(2) 연장기간 (yy.mm.dd ~ yy.mm.dd)
st.subheader("광고 연장 기간을 입력해주세요.")
start_date = st.date_input('광고 종료일을 선택해주세요.')
deadline = st.date_input('광고 연장일을 선택해주세요.')
    
 #(3) 광고 기간 계산
start_date = parser.parse(str(start_date))
deadline = parser.parse(str(deadline))
dur = (deadline - start_date).days
if (dur <= 0): st.error("광고기간 입력 오류입니다. 입력한 광고 종료일과 연장일을 다시 한 번 확인해주세요.")