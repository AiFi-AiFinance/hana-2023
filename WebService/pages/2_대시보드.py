# 대시보드: 로그인한 기업의 광고 리스트 보여주기

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

import numpy as np
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

        
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