## 광고 관리 페이지

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