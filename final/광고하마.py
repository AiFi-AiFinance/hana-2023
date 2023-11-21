## 광고하마 시작페이지

## 기업 회원가입 및 로그인
# PostgreSQL 데이터 베이스 연동
import psycopg2
connection = psycopg2.connect(host="34.42.241.68", dbname="hana-2023-database", user="postgres", password="1234", port=5432)
cur = connection.cursor()

# store_code를 얻는 함수
def get_store_code():
    try:
        cur.execute("SELECT COUNT(*) FROM company;")
        result = cur.fetchone()
        if result:
            return result[0]  # Return the count value
        else:
            return 0  # Return 0 if no count value obtained
    except Exception as e:
        print("Error fetching store count:", e)
        return None 
    
# 회원가입 시 company 테이블 insert
def insert_company(store_name,email,passwd,phone):
    store_code = get_store_code()
    try:
        cur.execute("INSERT INTO company (store_code,store_name,email,passwd,phone) VALUES (%d, %s, %s, %s, %s);",
            (store_code,store_name,email,passwd,phone)
            )
        connection.commit()
        store_code += 1
    except Exception as e:
        print("회원가입 에러:", e)
    return None  # 회원가입 실패 

# 현재 로그인 되어있는 기업의 코드
cur_store = 0
def get_cur_store():
    global cur_store
    return cur_store

# 로그인 시 비밀번호 확인
def login_company(email, passwd):
    global cur_store
    try:
        cur.execute("SELECT store_name, store_code, passwd FROM company WHERE email = %s;", (email,))
        result = cur.fetchone()  # 단일 행을 가져옵니다.
        if result:  # 결과가 있는 경우에만 비밀번호 검증 수행
            stored_password = result[2]  # company 테이블의 비밀번호 필드 (0부터 시작하는 인덱스)
            if passwd == stored_password:  # 비밀번호 일치 확인
                cur_store = int(result[1])  # store_code 설정
                return result[0]  # store_name 반환
    except Exception as e:
        print("로그인 에러:", e)
    return None  # 로그인 실패

# streamlit 광고하마 시작페이지 기본설정
import streamlit as st
st.set_page_config(page_icon="🦛", page_title="광고하마 시작페이지")
st.subheader("사장님의 하나뿐인 마케터,")
st.header("광고하마입니다. 🦛")

# 현재 기업 로그인 여부
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# 페이지 관리
from st_pages import Page, hide_pages, show_pages
show_pages(
    [
        Page("final/pages/1_대시보드.py", "대시보드", "📋"),
        Page("final/pages/2_광고신청.py", "광고신청", "📄"),
        Page("final/pages/3_추천멘트.py", "추천멘트", "🤖"), 
        Page("final/pages/4_광고리포트.py", "광고리포트", "💁🏼‍♀️")
    ]
)   

if st.session_state["logged_in"] == False:
    hide_pages( ["광고하마","대시보드","광고신청","추천멘트","광고리포트"])
    
# 기업 로그인
st.write("-----")
st.subheader("로그인")
email = st.text_input("이메일(id)",placeholder="이메일(id)을 입력해주세요.",key=1)
passwd = st.text_input("비밀번호",placeholder="비밀번호를 입력해주세요.", type="password",key=2)

# GPT 수정
# 사용자가 입력한 비밀번호를 해시화한 후 로그인 시 비교
if st.button("로그인", type="primary"):
    if email == "":
        st.warning("잘못된 이메일(id)입니다.")
    elif passwd == "":
        st.warning("잘못된 비밀번호입니다.")
    else:
        store_name = login_company(email, passwd)  # 수정된 login_company 함수 호출
        if store_name:
            st.session_state["logged_in"] = True
            st.success(f"로그인 성공 {store_name}")  # store_name 출력
        else:
            st.warning("잘못된 로그인 정보입니다.")

# 로그인시 서비스 페이지 노출 
if st.session_state["logged_in"] == True:
    hide_pages([])
    
# 회원 가입 버튼 입력 여부
if "button_in" not in st.session_state:
    st.session_state["button_in"] = False
    
# 기업 회원가입 버튼
if st.button("회원가입"):
    st.session_state["button_in"] = True
    
if st.session_state["button_in"] == True:
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
            insert_company(new_company, new_email, new_passwd, new_phone, new_passwd)
            st.success("회원가입 완료, 로그인해주세요.")
            st.session_state["button_in"] = False