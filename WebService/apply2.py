from lib2to3.pgen2.pgen import DFAState
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


#------------아래는 제목-----------------
    

#제목
col1,empty2,col2 = st.columns([1, 0.3, 8.7])


    

with col2 :
    st.title("기업 광고 신청페이지\n")


#------------아래는 입력 (총 13개)---------

col1,empty2,col2 = st.columns([1, 0.03, 1])

#(1) 업체명 이메일 전화번호 비밀번호
with col1 :
    st.subheader("기업 정보")
    store_name = st.text_input('업체명을 입력해주세요.', value="")
    email = st.text_input('이메일을 입력해주세요.', value="")
    phone = st.text_input('전화번호를 입력해주세요.', value="")
    passwd = st.text_input('비밀번호를 입력해주세요.', value="", type='password')
    
#(2) 광고 텍스트 (~원)
with col2 :
    st.subheader("광고 정보")
    title = st.text_input('광고 제목을 입력해주세요.', value="")
    contents = st.text_area('광고 내용을 입력해주세요.', value="")
    


#(2) 카테고리 summary (건축~)
with col2 :
    summary = ['선택해주세요', '문화/생활', '여행/해외', '쇼핑/무이자', '정기결제', '할인/캐시백', '응모/경품', 'QR 결제']
    selected_summary = st.selectbox('카테고리',summary)
string = '광고 종류_'
DFAState.loc[string + selected_summary] = 1.0


#(3) 이미지 넣기 (~원)
with col2 :
    image = st.file_uploader('이미지를 업로드 하세요.', type=['png', 'jpg', 'jpeg'])
    
#(4) 광고기간 (yy.mm.dd ~ yy.mm.dd)
with col2 :
    start_date = st.date_input('광고 시작일을 선택해주세요.')
with col2 :
    deadline = st.date_input('광고 종료일을 선택해주세요.')
    
 #(5) 광고 기간 계산
start_date = parser.parse(str(start_date))
deadline = parser.parse(str(deadline))
dur = (deadline - start_date).days
if (dur <= 0): st.error("광고기간 입력 오류입니다. 입력한 광고 시작일과 종료일을 다시 한 번 확인해주세요.")
DFAState.loc['광고 기간'] = dur
   

