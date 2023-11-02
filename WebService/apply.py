import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pandas as pd
from PIL import Image

st.set_page_config(
        page_title="apply",
        page_icon="dart",
        layout="wide",
    )
#제목
image = Image.open('phoneix.png')
col1,empty2,col2 = st.columns([1, 0.3, 8.7])
with col1:
    st.image(image)
with col2:
    st.title("광고 신청 페이지\n")


# ------------------------------------
#입력받은 정보를 pandas의 DataFrame으로 저장해서 return해주는 함수
def ad_apply():
    apply = pd.DataFrame
    return apply