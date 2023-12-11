# 회원 가

# 페이지 기본 설정
import streamlit as st
st.set_page_config(page_title="광고하마 회원가입",page_icon="🦛",layout="centered")
st.subheader("광고하마 회원가입 페이지 입니다.")
st.text("왼쪽에서 로그인 하실 수 있습니다.")
st.markdown("***")

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

# 사이드바
with st.sidebar:
    # 기업 로그인
    st.subheader("로그인")
    email = st.text_input("이메일(ID)",placeholder="이메일(ID)을 입력해주세요.",key=5)
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
            store_code, store_name = "1", "아이러브카페"  # login_company 함수 호출
            if store_code and store_name:
                st.session_state["logged_in"] = True
                #log.set_cur_store(store_code)
                st.success(f"로그인 성공 {store_name}")  # store_name 출력
            else:
                st.warning("잘못된 로그인 정보입니다.")
            
# 로그인시 서비스 페이지 노출 
# if st.session_state["logged_in"] == True:
#     hide_pages(["회원가입","광고연장"])
    
st.write("-----")
st.subheader("회원가입")
new_company = st.text_input("기업명", placeholder="기업명을 입력해주세요.")
new_email = st.text_input("이메일(id)", placeholder="이메일(id)을 입력해주세요.", key=3)
new_passwd = st.text_input("비밀번호", placeholder="비밀번호를 입력해주세요.", type="password", key=4)
new_phone = st.text_input("연락처", placeholder="연락처를 입력해주세요.")

if st.button("회원가입",type="primary"):
    if new_company == "":  
        st.warning("잘못된 기업명 입니다.")
    elif new_email == "":  
        st.warning("잘못된 이메일(id) 입니다.")
    elif new_passwd == "":  
        st.warning("잘못된 비밀번호 입니다.")
    elif new_phone == "":  
        st.warning("잘못된 연락처 입니다.")
    else:
        # insert_company(new_company, new_email, new_passwd, new_phone, new_passwd)
        st.success("회원가입 완료, 로그인해주세요.")
        st.session_state["button_in"] = False