## 광고하마 시작페이지

# 기업 회원가입 및 로그인 데이터베이스
import psycopg2
class Database():
    # PostgreSQL 데이터 베이스 서버 연결
    connection = psycopg2.connect(host="34.42.241.68", dbname="hana-2023-database", user="postgres", password="1234", port=5432)
    cur = connection.cursor()

    # store_code: 현재 company 테이블에 있는 데이터의 수 +1
    # store_code를 반환하는 함수
    def get_store_code(self):
        try:
            self.cur.execute("SELECT COUNT(*) FROM company;")
            result = self.cur.fetchone()
            if result:
                return result[0] +1 
            else:
                return 1
        except Exception as e:
            print("Error fetching store count:", e)
            return None 
        
    # 회원가입 시 company 테이블에 데이터 insert하는 함수
    def insert_company(self,store_name,email,passwd,phone):
        store_code = self.get_store_code()
        try:
            self.cur.execute("INSERT INTO company (store_code,store_name,email,passwd,phone) VALUES (%d, %s, %s, %s, %s);",
                (store_code,store_name,email,passwd,phone)
                )
            self.connection.commit()
        except Exception as e:
            print("insert error:", e)
        return None

    # 로그인 시 비밀번호 확인
    def login_company(self,email,passwd):
        try:
            self.cur.execute("SELECT store_code, store_name, passwd FROM company WHERE email = %s;", (email,))
            result = self.cur.fetchone()  # 단일 행을 가져옵니다.
            if result:  # 결과가 있는 경우에만 비밀번호 검증 수행
                stored_password = result[2]  # company 테이블의 비밀번호 필드 (0부터 시작하는 인덱스)
                if passwd == stored_password:  # 비밀번호 일치 확인
                    return result[0], result[1]  # store_code, store_name 반환
        except Exception as e:
            print("select error:", e)
        return None
    
class Log():
    cur_store = 0
    
    def get_cur_store(self):
        return self.cur_store
    
    def set_cur_store(self,store_code):
        self.cur_store = store_code

# streamlit 광고하마 로그인페이지 기본설정
import streamlit as st
st.set_page_config(page_title="광고하마 로그인페이지",page_icon="🦛",layout="centered",initial_sidebar_state="collapsed")
st.subheader("사장님의 하나뿐인 마케터,")
st.header("광고하마입니다. 🦛")

# 현재 기업 로그인 여부
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    
# 페이지관리
from st_pages import hide_pages
if st.session_state["logged_in"] == False:
    hide_pages( ["대시보드","광고신청","추천멘트","고객분석"])

# 데이터 베이스 클래스 불러오기
db = Database()

# Log 클래스 불러오기
log = Log()
    
# 기업 로그인
st.write("-----")
st.subheader("로그인")
email = st.text_input("이메일(id)",placeholder="이메일(id)을 입력해주세요.",key=1)
passwd = st.text_input("비밀번호",placeholder="비밀번호를 입력해주세요.", type="password",key=2)

# 로그인 정보 확인
if st.button("로그인", type="primary"):
    if email == "":
        st.warning("잘못된 이메일(id)입니다.")
    elif passwd == "":
        st.warning("잘못된 비밀번호입니다.")
    else:
        store_code, store_name = db.login_company(email, passwd)  # login_company 함수 호출
        if store_code and store_name:
            st.session_state["logged_in"] = True
            log.set_cur_store(store_code)
            st.success(f"로그인 성공 {store_name}")  # store_name 출력
        else:
            st.warning("잘못된 로그인 정보입니다.")

# 로그인시 서비스 페이지 노출 
if st.session_state["logged_in"] == True:
    hide_pages([])
    
# 회원가입 버튼 입력 여부
if "button_in" not in st.session_state:
    st.session_state["button_in"] = False
    
# 기업 회원가입 버튼
if st.button("회원가입"):
    st.session_state["button_in"] = True

# 회원가입 버튼이 눌러졌을 때, 입력창 생성
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
            db.insert_company(new_company, new_email, new_passwd, new_phone, new_passwd)
            st.success("회원가입 완료, 로그인해주세요.")
            st.session_state["button_in"] = False