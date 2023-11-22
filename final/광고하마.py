# streamlit 광고하마 시작페이지 기본설정
import streamlit as st
st.set_page_config(page_title="광고하마 시작페이지",page_icon="🦛",layout="centered",initial_sidebar_state="expanded")
st.subheader("사장님의 하나뿐인 마케터,")
st.header("광고하마입니다. 🦛")

# 페이지 관리
from st_pages import Page, hide_pages, show_pages
show_pages(
    [
        Page("final/광고하마.py", "광고하마", "🦛"),
        Page("final/pages/login.py", "로그인", "🖐️"),
        Page("final/pages/dashboard.py", "대시보드", "📋"),
        Page("final/pages/apply.py", "광고신청", "📄"),
        Page("final/pages/recommend.py", "추천멘트", "🤖"), 
        Page("final/pages/target.py", "고객분석", "💁🏼‍♀️")
    ]
) 

hide_pages(["대시보드","광고신청","추천멘트","고객분석"])