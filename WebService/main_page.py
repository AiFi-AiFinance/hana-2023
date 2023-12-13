import sys
sys.path.append("..")
# from database.login import *
# from utils.store_code import *
def login_company(email, passwd):
    if email == "sheep@naver.com" and passwd == "1234":
        return 1, "승연이네"
    elif email == "annkwon1123@naver.com" and passwd == "1234":
        return 2, "아이러브카페"
    else:
        return None
    
class Log():
    cur = 0
    def set_cur_store(self, store_code):
        self.cur = store_code
    
    def get_store_code(self):
        return self.cur
        
log = Log()

# streamlit 광고하마 시작페이지 기본설정
import streamlit as st
from PIL import Image
st.set_page_config(page_title="광고하마 시작페이지",page_icon="🦛",layout="wide")

# 페이지 헤더, 서브헤더 제목 설정
col1,empty2,col2 = st.columns([1, 0.1, 8.9])

with col1:
    image_logo = Image.open('aifi_logo.png')
    st.image(image_logo, width=100)
    
with col2:
    st.markdown(f'<h1 style="color:#008485;font-size:54px;">{"하나뿐인 마케터, 광고하마"}</h1>', unsafe_allow_html=True)
    st.text("왼쪽에서 로그인 후 광고하마를 이용하실 수 있습니다.\n\n")
    
st.markdown("***")

# 페이지 관리
# from st_pages import Page, hide_pages, show_pages
# show_pages(
#     [
#         Page("WebService/main_page.py", "광고하마", "🦛"),
#         Page("WebService/pages/1_회원가입.py", "회원가입", "🖐️"),
#         Page("WebService/pages/2_대시보드.py", "대시보드", "📋"),
#         Page("WebService/pages/3_광고신청.py", "광고신청", "📄"),
#         Page("WebService/pages/4_추천멘트.py", "추천멘트", "🤖"), 
#         Page("WebService/pages/5_고객분석.py", "고객분석", "💁🏼‍♀️")
#     ]
# ) 

# 현재 기업 로그인 여부
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    
# 페이지관리
# from st_pages import hide_pages
# if st.session_state["logged_in"] == False:
#     hide_pages( ["대시보드","광고신청","추천멘트","고객분석","광고연장"])
    
# 로그인 버튼 입력 여부
if "button_login" not in st.session_state:
    st.session_state["button_login"] = False
    
with st.sidebar:
    # 기업 로그인
    st.subheader("로그인")
    email = st.text_input("이메일(id)",placeholder="이메일(id)을 입력해주세요.",key=5)
    passwd = st.text_input("비밀번호",placeholder="비밀번호를 입력해주세요.", type="password",key=6)
    if st.button("로그인", type="primary",key=8):
        st.session_state["button_login"] = True

    # 로그인 정보 확인  
    if st.session_state["button_login"] == True:
        if email == "":
            st.warning("잘못된 이메일(id)입니다.")
        elif passwd == "":
            st.warning("잘못된 비밀번호입니다.")
        else:
            store_code, store_name = login_company(email, passwd)  # login_company 함수 호출
            if store_code and store_name:
                st.session_state["logged_in"] = True
                log.set_cur_store(store_code)
                st.success(f"로그인 성공: {store_name} 사장님 안녕하세요!")  # store_name 출력
            else:
                st.warning("잘못된 로그인 정보입니다.")
            
# 로그인시 서비스 페이지 노출 
# if st.session_state["logged_in"] == True:
#     hide_pages(["회원가입","광고연장"])

# 상세페이지
image001 = Image.open('001.png')
st.image(image001)
image002 = Image.open('002.png')
st.image(image002)
image003 = Image.open('003.png')
st.image(image003)
image004 = Image.open('004.png')
st.image(image004)
image005 = Image.open('005.png')
st.image(image005)
image006 = Image.open('006.png')
st.image(image006)
image_aifi = Image.open('aifi.jpg')
st.image(image_aifi)
    