## 광고 관리 페이지

## 광고 
# store_code 불러오기
import sys
sys.path.append("..")
from final.광고하마 import get_cur_store
cur_store = get_cur_store()

# PostgreSQL 데이터 베이스 연동
import psycopg2
connection = psycopg2.connect(host="34.42.241.68", dbname="hana-2023-database", user="postgres", password="1234", port=5432)
cur = connection.cursor()

# 현재 기업 정보
def get_company():
    global cur_store
    try:
        cur.execute("SELECT store_name,email,phone FROM company WHERE store_code = %d;", (cur_store,))
        result = cur.fetchone()  # 단일 행을 가져옵니다.
        return result 
    except Exception as e:
        print("기업정보 에러:", e)
    return None 

# 현재 기업의 신청한 광고 개수
def get_ad_num():
    global cur_store
    try:
        cur.execute("SELECT COUNT(*) FROM advertisement WHERE store_code = %d;", (cur_store,))
        result = cur.fetchone()  # 단일 행을 가져옵니다.
        if result:
            return result[0]  # Return the count value
        else:
            return 0  # Return 0 if no count value obtained
    except Exception as e:
        print("광고숫자정보 에러:", e)
    return None

# 현재 기업의 신청한 광고 
def get_ad():
    global cur_store
    try:
        cur.execute("SELECT title,contents,category,keyword,image,start_date,deadline FROM advertisement WHERE store_code = %d;", (cur_store,))
        result = cur.fetchone()  # 단일 행을 가져옵니다.
        return result
    except Exception as e:
        print("광고정보 에러:", e)
    return None 

# streamlit 광고하마 광고신청 페이지 기본설정
import streamlit as st
st.set_page_config(page_icon="🦛", page_title="광고하마 대시보드", layout="wide")
st.subheader("사장님의 하나뿐인 마케터,")
st.header("광고하마입니다. 🦛")

# 차트 그리기
import pandas as pd
import numpy as np


# 매칭 정도
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)