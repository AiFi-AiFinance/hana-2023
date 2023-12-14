# 인플루언서: 

# 페이지 기본 설정
import streamlit as st
# from st_pages import hide_pages
from PIL import Image
st.set_page_config(page_title="광고하마 인플루언서 제안",page_icon="🦛",layout="wide")
# hide_pages(["회원가입","광고연장"])
st.subheader("광고하마에서 제안하는 인플루언서입니다.")
st.text("현재 광고는 아이러브커피 매장의 수정과입니다.")
st.markdown("***")

# 사이드바
with st.sidebar:
    st.text("아이러브커피")
    image005 = Image.open('005.png')
    st.image(image005)
    
# 페이지 내용  
# 로그인한 기업이 가진 광고의 추천멘트
ments = [
    "귀엽고 따뜻한 곰돌이 모자, 포근함을 선사합니다",
    "귀여움 가득, 겨울을 따뜻하게 감싸는 곰돌이 모자",
    "귀여운 디자인으로 따뜻함을 더한 곰돌이 모자"
    ]
col1,col2,col3 = st.columns(3)
with col1:
     with st.chat_message("user",avatar="🍀"):
          st.write("[ 블로거 소여닐기 ]")
          st.write(ments[0])
     st.write("      이웃 수: 19천 명")
     st.write("일간 방문자 수: 256 명")
     st.write("      전체 글: 125 개") 
     if st.button("선택"):
         st.success("해당 인플루언서가 선택 되었습니다.")
    
with col2:
     with st.chat_message("user",avatar="🥕"):
         st.write("[ 당근러 수박대박 ]")
         st.write(ments[1])
     st.write("   누적 이용자 수: 13천 명")
     st.write("월 평균 이용자 수: 600 명")
     st.write("   월 평균 조회수: 3.4천 회")
     if st.button("선택", key=2):
        st.success("해당 인플루언서가 선택 되었습니다.") 

with col3:
     with st.chat_message("user",avatar="🍽️"):
         st.write("[ 유튜버 1분요리 ]")
         st.write(ments[2])
     st.write("구독자 수: 12만 명") 
     st.write("평균 조회수: 7.8천 회")
     st.write("전체 동영상: 37 개")
     if st.button("선택",key=3):
        st.success("해당 인플루언서가 선택 되었습니다.") 