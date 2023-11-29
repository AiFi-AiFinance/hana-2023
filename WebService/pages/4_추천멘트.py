# 추천멘트: 

# 페이지 기본 설정
import streamlit as st
from st_pages import hide_pages
from PIL import Image
st.set_page_config(page_title="광고하마 추천멘트",page_icon="🦛",layout="centered")
hide_pages(["회원가입","광고연장"])
st.subheader("광고하마 친구들이 제안하는 광고 추천 멘트입니다.")
st.text("현재 광고는 아이러브커피 매장의 수정과입니다.")
st.markdown("***")

# 사이드바
with st.sidebar:
    st.text("아이러브커피")
    image006 = Image.open('006.png')
    st.image(image006)
    
# 페이지 내용  
# 로그인한 기업이 가진 광고의 추천멘트
ments = [
    "겨울을 더욱 스타일리시하게! 모자 가게에서 트렌디한 모자를 만나보세요.",
    "패션에는 세부사항이 중요합니다. 모자 가게에서 다양한 스타일의 모자를 찾아보세요.",
    "모자 가게에서는 겨울에 딱 맞는 따뜻하고 멋진 모자를 만나실 수 있습니다. 지금 바로 방문해보세요!"
    ]

with st.chat_message("user",avatar="🦛"):
    st.write("[ 광고하마 추천 멘트 ]")
    st.write(f"안녕하세요, 광고하마 입니다. 제가 추천하는 광고멘트입니다. {ments[0]}")
    if st.button("멘트 선택"):
        st.success("광고 멘트가 업데이트 되었습니다.")
    
with st.chat_message("user",avatar="🐻"):
    st.write("[ 광곰 추천 멘트 ]")
    st.write(f"안녕하세요, 광곰 입니다. 제가 추천하는 광고멘트입니다. {ments[1]}")
    if st.button("멘트 선택", key=2):
        st.success("광고 멘트가 업데이트 되었습니다.") 

with st.chat_message("user",avatar="🐶"):
    st.write("[ 광아지 추천 멘트 ]")
    st.write(f"안녕하세요, 광아지 입니다. 제가 추천하는 광고멘트입니다. {ments[2]}")
    if st.button("멘트 선택",key=3):
        st.success("광고 멘트가 업데이트 되었습니다.") 
    
st.write("추천 멘트가 마음에 들지 않으시면, 멘트를 직접 입력하거나 새로 고침을 하실 수 있습니다.")
prompt = st.chat_input("원하는 멘트를 작성해 주세요.")
if prompt:
    with st.chat_message("user"):
        st.write("[ 직접입력 ]")
        st.write(f"{prompt}")
        if st.button("멘트 선택",key=4):
            st.success("광고 멘트가 업데이트 되었습니다.") 