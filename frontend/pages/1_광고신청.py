## 광고신청 페이지

## 광고신청
# store_code 불러오기
import sys
sys.path.append("..")
from frontend.광고하마 import get_cur_store
store_code = get_cur_store()

# PostgreSQL 데이터 베이스 연동
import psycopg2
connection = psycopg2.connect(host="34.42.241.68", dbname="hana-2023-database", user="postgres", password="1234", port=5432)
cur = connection.cursor()

ad_code = 1
# 광고 신청시 advertisement 테이블 insert
def insert_ad(title,contents,category,keyword,image,start_date,deadline):
    global ad_code, store_code
    cur.execute("INSERT INTO advertisement (ad_code,store_code,title,contents,category,keyword,image,start_date,deadline) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);",
        (ad_code,store_code,title,contents,category,keyword,image,start_date,deadline)
        )
    connection.commit()
    ad_code += 1

# streamlit 광고하마 광고신청 페이지 기본설정
import streamlit as st
st.set_page_config(page_icon="🦛", page_title="광고하마 메인페이지", layout="wide")
st.subheader("사장님의 하나뿐인 마케터,")
st.header("광고하마입니다. 🦛")
    
# 광고 신청
st.write("-----")
st.subheader("광고신청")
col1,col2 = st.columns(2)
with col1:
    title = st.text_input("광고 제목",placeholder="광고 제목을 입력해주세요.")
    contents = st.text_area("광고 내용",placeholder="광고 내용을 입력해주세요.")
    category = ['카테고리 선택','문화/생활', '여행/해외', '쇼핑/무이자', '정기결제', '할인/캐시백', '응모/경품', 'QR 결제']
    selected_category = st.selectbox("카테고리",options=category,placeholder="카테고리를 선택해주세요.")
    
with col2:
    keyword = st.text_input("키워드",placeholder="\' , \'로 구분해서 입력해주세요.")
    image = st.file_uploader("이미지", type=['png', 'jpg', 'jpeg'])
    start_date = st.date_input("광고 시작일")
    deadline = st.date_input("광고 종료일")
    
    from dateutil import parser
    start_date = parser.parse(str(start_date))
    deadline = parser.parse(str(deadline))
    dur = (deadline - start_date).days
    if (dur <= 0): st.error("광고 기간 입력 오류입니다. 입력한 광고 시작일과 종료일을 다시 한 번 확인해 주세요.")

if st.button("광고신청",type="primary"):
    if title == "":  
        st.warning("잘못된 광고 제목 입니다.")
    elif contents == "":  
        st.warning("잘못된 광고 내용 입니다.")
    elif selected_category == "":  
        st.warning("잘못된 카테고리 입니다.")
    elif keyword == "":  
        st.warning("잘못된 키워드 입니다.")
    else:
        insert_ad(title,contents,category,keyword,image,start_date,deadline)
        st.success("광고신청 완료")

# 데이터 베이스 종료
cur.close()
connection.close()