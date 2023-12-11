# 대시보드: 로그인한 기업의 광고 리스트 보여주기

# 페이지 기본 설정
import streamlit as st
# from st_pages import hide_pages
st.set_page_config(page_title="광고하마 대시보드",page_icon="🦛",layout="wide")
# hide_pages(["회원가입","광고연장"])
st.subheader("하나뿐인 마케터에 신청한 광고입니다.")
st.text("현재 로그인 된 매장은 아이러브커피입니다.")
st.markdown("***")

# 사이드바
with st.sidebar:
  st.text("아이러브커피")
  
# 페이지 내용 
import streamlit as st
from datetime import datetime, timedelta
 
# 일주일 범위의 datetime slider 생성
start_date = datetime(2023, 11, 1)
end_date = start_date + timedelta(weeks=1)
 
selected_date = st.slider(
    "날짜 범위 선택",
    min_value=start_date,
    max_value=end_date,
    value=(start_date, end_date),
    step=timedelta(days=1),
)

        
# 페이지
col1,col2,col3 = st.columns(3)
with col1:
    with st.expander("겨울 모자 광고"):
        st.write("겨울 모자 광고")
        st.bar_chart(chart_data)

with col2:  
    with st.expander("수정과 광고"):
        st.write("겨울 모자 광고")
        st.line_chart(chart_data) 
        
with col3:  
    with st.expander("수과 광고"):
        st.write("겨울 모자 광고")
        st.line_chart(chart_data) 