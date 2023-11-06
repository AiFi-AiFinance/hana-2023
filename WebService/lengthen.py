import streamlit as st
import numpy as np
import pandas as pd

# ------------------------------------
# 입력받은 정보를 pandas의 DataFrame으로 저장해서 return해주는 함수
def ad_date():
    date = pd.DataFrame
    return date
# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import re
from dateutil import parser


col1,empty2,col2 = st.columns([1, 0.3, 8.7])





with col2 :
    st.title("기업 광고 연장페이지\n")



col1,empty2,col2 = st.columns([1, 0.03, 1])

#(1) 기업 정보
with col1 :
    st.subheader("기업 정보")
    store_name = st.text_input('업체명을 입력해주세요.', value="")
    passwd = st.text_input('비밀번호를 입력해주세요.', value="", type='password')
    

#(2) 연장기간 (yy.mm.dd ~ yy.mm.dd)
with col2 :
    st.subheader("광고 정보")
with col2 :
    start_date = st.date_input('광고 종료일을 선택해주세요.')
with col2 :
    deadline = st.date_input('광고 연장일을 선택해주세요.')
    
 #(3) 광고 기간 계산
start_date = parser.parse(str(start_date))
deadline = parser.parse(str(deadline))
dur = (deadline - start_date).days
if (dur <= 0): st.error("광고기간 입력 오류입니다. 입력한 광고 종료일과 연장일을 다시 한 번 확인해주세요.")
df.loc['광고 기간'] = dur

 
