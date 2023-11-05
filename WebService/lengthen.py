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


#(1) 연장기간 (yy.mm.dd ~ yy.mm.dd)
with col2 :
    start_date = st.date_input('광고 종료일을 선택해주세요.')
with col2 :
    deadline = st.date_input('광고 연장일을 선택해주세요.')
    
 #(2) 광고 기간 계산
start_date = parser.parse(str(start_date))
deadline = parser.parse(str(deadline))
dur = (deadline - start_date).days
if (dur <= 0): st.error("광고기간 입력 오류입니다. 입력한 광고 종료일과 연장일을 다시 한 번 확인해주세요.")
df.loc['광고 기간'] = dur

   
