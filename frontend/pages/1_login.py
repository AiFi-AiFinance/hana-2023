import hashlib
import json
import psycopg2
from pathlib import Path
import pandas as pd

# 스트림릿을 사용하기 위한 설정
import streamlit as st
from streamlit.source_util import _on_pages_changed, get_pages
from streamlit_extras.switch_page_button import switch_page

DEFAULT_PAGE = "1_login.py"
SECOND_PAGE_NAME = "hana_marketer.py"


def get_all_pages():
    default_pages = get_pages(DEFAULT_PAGE)

    pages_path = Path("pages.json")

    if pages_path.exists():
        saved_default_pages = json.loads(pages_path.read_text())
    else:
        saved_default_pages = default_pages.copy()
        pages_path.write_text(json.dumps(default_pages, indent=4))

    return saved_default_pages


def clear_all_but_first_page():
    current_pages = get_pages(DEFAULT_PAGE)

    if len(current_pages.keys()) == 1:
        return

    get_all_pages()

    # 기업 로그인 페이지를 제외한 페이지 숨기기
    key, val = list(current_pages.items())[0]
    current_pages.clear()
    current_pages[key] = val

    _on_pages_changed.send()


def show_all_pages():
    current_pages = get_pages(DEFAULT_PAGE)

    saved_pages = get_all_pages()

    # 모든 페이지 보이게 하기
    for key in saved_pages:
        if key not in current_pages:
            current_pages[key] = saved_pages[key]

    _on_pages_changed.send()


def hide_page(name: str):
    current_pages = get_pages(DEFAULT_PAGE)

    for key, val in current_pages.items():
        if val["page_name"] == name:
            del current_pages[key]
            _on_pages_changed.send()
            break


clear_all_but_first_page()


# 비밀번호를 해시 형태로 바꾸기
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

# 비밀번호가 맞는지 확인하기
def check_hashes(password, hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

# DB 관리 클래스
class Databases():
    # 구글 클라우드에서 호스팅 하는 postgreSQL 연결
    def __init__(self):
        self.db = psycopg2.connect(host='34.42.241.68', dbname='hana-2023-database',user='postgres',password='1234',port=5432)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()
        self.cursor.close()
        
    # SQL 명령어를 처리하기 위한 execute 함수
    def execute(self,query,args={}):
        self.cursor.execute(query,args)
        row = self.cursor.fetchall()
        return row
    
    # transaction 변화를 commit 하는 함수
    def commit(self):
        self.cursor.commit()

# 기업정보 로그인를 위해 데이터를 SQL문으로 바꾸는 클래스
class CRUD_company(Databases):
    store_code = 1
    
    # 기업 정보 입력
    def insert_company(self,store_name,email,passwd,phone):
        sql = " INSERT INTO company(store_code,store_name,email,password,phone) VALUES (?,?,?,?,?) "
        try:
            self.cursor.execute(sql,(self.store_code,store_name,email,passwd,phone))
            self.db.commit()
            self.store_code += 1
        except Exception as e :
            print(" insert DB err ",e) 
    
    # 기업 로그인
    def login_company(self,email,passwd):
        sql = " SELECT * FROM company WHERE email =? AND password = ? "
        try:
            self.cursor.execute(sql,(email,passwd))
            result = self.cursor.fetchall()
        except Exception as e :
            result = (" read DB err",e)
        
        return result
    
    # 기업 테이블 전체 읽기
    def view_table(self):
        sql = " SELECT * FROM company "
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e :
            result = (" read DB err",e)
        
        return result

    def updateDB(self,schema,table,colum,value,condition):
        sql = " UPDATE {schema}.{table} SET {colum}='{value}' WHERE {colum}='{condition}' ".format(schema=schema
        , table=table , colum=colum ,value=value,condition=condition )
        try :
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e :
            print(" update DB err",e)

    def deleteDB(self,schema,table,condition):
        sql = " delete from {schema}.{table} where {condition} ; ".format(schema=schema,table=table,
        condition=condition)
        try :
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print( "delete DB err", e)
            

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False


# 메인 스트림릿
def main():
    # 로그인 페이지
    st.title("환영합니다! 광고하마 입니다. ")
    menu = ["로그인", "회원가입"]
    choice = st.selectbox(
        "아래에서 로그인 또는 회원가입 버튼을 입력해주세요. ▾",
        menu,
    )
    st.markdown(
        "<h10 style='text-align: left; color: #ffffff;'> 광고하마에 처음 오셨나요? 회원가입 버튼을 눌러주세요.</h10>",
        unsafe_allow_html=True,
    )
    
    db = CRUD_company()
    
    if choice == "":
        st.subheader("로그인")
    elif choice == "로그인":
        st.write("-------")
        st.subheader("로그인이 필요합니다. ")

        email = st.text_input("기업명", placeholder="email")
        passwd = st.text_input("비밀번호", type="password")
        
        if st.checkbox("로그인"):
            # if password == '1234':
            # Hash password creation and store in a table
            hashed_pswd = make_hashes(passwd)
            
            result = db.login_company(email, check_hashes(passwd, hashed_pswd))
            if result:
                st.session_state["logged_in"] = True
                st.success("로그인 되었습니다. {}".format(email))

                if st.success:
                    st.subheader("기업 정보 ")
                    user_result = db.view_table()
                    clean_db = pd.DataFrame(
                        user_result, columns=["store_code","store_name","email","passwd","phone"]
                    )
                    st.dataframe(clean_db)
            else:
                st.warning("잘못된 접근입니다. 로그인 정보를 확인해 주세요. ")
    elif choice == "회원가입":
        st.write("-----")
        st.subheader("기업 정보를 입력해주세요. ")
        new_company = st.text_input("기업명", placeholder="name")
        new_email = st.text_input("이메일 id", placeholder="email")
        new_passwd = st.text_input("비밀번호", type="password")
        new_phone = st.text_input("연락처", placeholde="phone number")

        if st.button("회원가입"):
            if new_company == "":  # if user name empty then show the warnings
                st.warning("Inavlid user name")
            elif new_email == "":  # if email empty then show the warnings
                st.warning("Invalid email id")
            elif new_passwd == "":  # if password empty then show the warnings
                st.warning("Invalid password")
            elif new_phone == "":  # if password empty then show the warnings
                st.warning("Invalid phone number")
            else:
                db.insert_company(new_company, new_email, new_passwd, new_phone, make_hashes(new_passwd))
                st.success("회원가입 완료")
                st.info("위에서 로그인 하세요. ")

    if st.session_state["logged_in"]:
        show_all_pages()
        hide_page(DEFAULT_PAGE.replace(".py", ""))
        switch_page(SECOND_PAGE_NAME)
    else:
        clear_all_but_first_page()


if __name__ == "__main__":
    main()