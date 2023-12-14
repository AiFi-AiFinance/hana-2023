# 광고 신청

# 페이지 기본 설정
import streamlit as st
# from st_pages import hide_pages
from PIL import Image
st.set_page_config(page_title="광고하마 광고 신청",page_icon="🦛",layout="wide")
# hide_pages(["회원가입","광고연장"])
st.subheader("광고하마에게 광고 신청하기!")
st.text("현재 로그인 된 매장은 아이러브커피입니다.")
st.markdown("***")

# 사이드바
with st.sidebar:
  st.text("아이러브커피")
  image002 = Image.open('002.png')
  st.image(image002)

# 데이터 베이스 순서대로 store_code 와 ad_code 불러오기
# from Database import get_store_code, get_ad_code
store_code = 1
ad_code = 1

# 광고 신청
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
    # insert_ad(title,contents,category,keyword,image,start_date,deadline)
    st.success("광고신청이 완료되었습니다.")
    
    
# 데이터 베이스 파일에서 insert
# def get_enterprise():
#   if store_code and store_name and email and phone and passwd:
#     return store_code, store_name, email, phone, passwd
#   else:
#     return -1

# GPT 파일에서 GPT_ad 받아오기
# 타입 분류 머신러닝 파일에서 타입 받아오기
# 그 다음에 데이터 베이스 파일에서 insert
# def get_advertisement():
#   if ad_code and store_code and title and contents and summary and image and start_date and deadline:
#     return ad_code, store_code, title, contents, summary, image, start_date, deadline
#   else:
#     return -1
