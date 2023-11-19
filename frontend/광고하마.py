## 광고하마 메인페이지

## 기업 회원가입 및 로그인
# PostgreSQL 데이터 베이스 연동
import psycopg2
connection = psycopg2.connect(host="34.42.241.68", dbname="hana-2023-database", user="postgres", password="1234", port=5432)
cur = connection.cursor()

store_code = 1
cur_store = 0
# 회원가입 시 company 테이블 insert
def insert_company(store_name,email,passwd,phone):
    global store_code
    cur.execute("INSERT INTO company (store_code,store_name,email,passwd,phone) VALUES (%s, %s, %s, %s, %s);",
        (store_code,store_name,email,passwd,phone)
        )
    connection.commit()
    store_code += 1

# 로그인한 기업의 store_code 반환 함수
def get_cur_store():
    global cur_store
    return cur_store

# 로그인 시 비밀번호 확인
def login_company(email,passwd):
    global cur_store
    try:
        cur.execute("SELECT * FROM company WHERE email=%s AND password=%s ;",
            (email,passwd)
            )
        result = cur.fetchall()
        cur_store = int(result[0][0])
    except Exception as e:
        result = ("SELECT ERROR", e)
    return result

# 비밀번호를 해시 형태로 바꾸기
import hashlib
def make_hashes(passwd):
    return hashlib.sha256(str.encode(passwd)).hexdigest()

# 비밀번호가 맞는지 확인하기
def check_hashes(passwd, hashed_text):
    if make_hashes(passwd) == hashed_text:
        return hashed_text
    return False

# streamlit 광고하마 메인페이지 기본설정
import streamlit as st
st.set_page_config(page_icon="🦛", page_title="광고하마 메인페이지")
st.subheader("사장님의 하나뿐인 마케터,")
st.header("광고하마입니다. 🦛")

# 현재 기업 로그인 여부
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    
# 기업 로그인
st.write("-----")
st.subheader("로그인")
email = st.text_input("이메일(id)",placeholder="이메일(id)을 입력해주세요.",key=1)
passwd = st.text_input("비밀번호",placeholder="비밀번호를 입력해주세요.", type="password",key=2)
    
if st.button("로그인",type="primary"):
    if email == "":  
        st.warning("잘못된 이메일(id) 입니다.")
    elif passwd == "":  
        st.warning("잘못된 비밀번호 입니다.")
    else:
        hashed_pswd = make_hashes(passwd)
        result = login_company(email, check_hashes(passwd, hashed_pswd))
        if result:
            st.session_state["logged_in"] = True
            st.success("로그인 성공 {}".format(email))
        else:
            st.warning("잘못된 로그인 정보입니다. ")

# 기업 회원가입
if st.button("회원가입"):
    st.write("-----")
    st.subheader("회원가입")
    new_company = st.text_input("기업명",placeholder="기업명을 입력해주세요.")
    new_email = st.text_input("이메일(id)",placeholder="이메일(id)을 입력해주세요.",key=3)
    new_passwd = st.text_input("비밀번호",placeholder="비밀번호를 입력해주세요.", type="password",key=4)
    new_phone = st.text_input("연락처",placeholder="연락처를 입력해주세요.")

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
            insert_company(new_company, new_email, new_passwd, new_phone, make_hashes(new_passwd))
            st.success("회원가입 완료, 사이드바에서 로그인해주세요.")

# 데이터 베이스 종료
cur.close()
connection.close()