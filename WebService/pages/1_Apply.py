## pages/1_Apply.py

# 데이터 베이스 순서대로 store_code 와 ad_code 불러오기
# from Database import get_store_code, get_ad_code
store_code = 1
ad_code = 1

# ------------------------ streamlit ------------------------ #
import streamlit as st
from dateutil import parser

# 페이지 기본 설정
st.set_page_config(
    page_icon="🐶",
    page_title="하나뿐인 마케터",
    layout="wide",
)

st.subheader("하나뿐인 마케터에 광고 신청하기")

col1,empty2,col2 = st.columns([1, 0.03, 1])

#(1) 업체명 이메일 전화번호 비밀번호
with col1 :
    st.subheader("기업 정보")
    store_name = st.text_input('업체명을 입력해주세요.', value="")
    email = st.text_input('이메일을 입력해주세요.', value="")
    phone = st.text_input('전화번호를 입력해주세요.', value="")
    passwd = st.text_input('비밀번호를 입력해주세요.', value="", type='password')
    
#(2) 광고
with col2 :
    st.subheader("광고 정보")
    title = st.text_input('광고 제목을 입력해주세요.', value="")
    contents = st.text_area('광고 내용을 입력해주세요.', value="")


#(2) 카테고리 summary
with col2 :
    summary = ['선택해주세요', '문화/생활', '여행/해외', '쇼핑/무이자', '정기결제', '할인/캐시백', '응모/경품', 'QR 결제']
    selected_summary = st.selectbox('카테고리',summary)

#(3) 이미지 넣기
with col2 :
    image = st.file_uploader('이미지를 업로드 하세요.', type=['png', 'jpg', 'jpeg'])
    
#(4) 광고기간 (yy.mm.dd ~ yy.mm.dd)
with col2 :
    start_date = st.date_input('광고 시작일을 선택해주세요.')
with col2 :
    deadline = st.date_input('광고 종료일을 선택해주세요.')
    
#(5) 광고 기간 계산
start_date = parser.parse(str(start_date))
deadline = parser.parse(str(deadline))
dur = (deadline - start_date).days
if (dur <= 0): st.error("광고기간 입력 오류입니다. 입력한 광고 시작일과 종료일을 다시 한 번 확인해주세요.")

# 데이터 베이스 파일에서 insert
def get_enterprise():
  if store_code and store_name and email and phone and passwd:
    return store_code, store_name, email, phone, passwd
  else:
    return -1

# GPT 파일에서 GPT_ad 받아오기
# 타입 분류 머신러닝 파일에서 타입 받아오기
# 그 다음에 데이터 베이스 파일에서 insert
def get_advertisement():
  if ad_code and store_code and title and contents and summary and image and start_date and deadline:
    return ad_code, store_code, title, contents, summary, image, start_date, deadline
  else:
    return -1

   
if st.button("광고 신청"):
    code = '''
    import streamlit as st
    import pandas터as pd
    import numpy as np
    from PIL import Image
    from time import sleep


    # 페이지 기본 설정
  st.set_page_config(
      page_icon="🐶",
      page_title="빅공잼의 스트림릿 배포하기",
      layout="wide",
  )

  # 로딩바 구현하기
  with st.spinner(text="페이지 로딩중..."):
      sleep(3)

  # 페이지 헤더, 서브헤더 제목 설정
  st.header("빅공잼 페이지에 오신걸 환영합니다👋")
  st.subheader("스트림릿 기능 맛보기")

  # 페이지 컬럼 분할(예: 부트스트랩 컬럼, 그리드)
  cols = st.columns((1, 1, 2))
  cols[0].metric("10/11", "15 °C", "2")
  cols[0].metric("10/12", "17 °C", "2 °F")
  cols[0].metric("10/13", "15 °C", "2")
  cols[1].metric("10/14", "17 °C", "2 °F")
  cols[1].metric("10/15", "14 °C", "-3 °F")
  cols[1].metric("10/16", "13 °C", "-1 °F")

  # 라인 그래프 데이터 생성(with. Pandas)
  chart_data = pd.DataFrame(
      np.random.randn(20, 3),
      columns=['a', 'b', 'c'])

  # 컬럼 나머지 부분에 라인차트 생성
  cols[2].line_chart(chart_data)
    '''
    st.code(code, language='python')