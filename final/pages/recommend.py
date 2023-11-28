import openai

openai.orgamization = 'org-DCXaZxUUjaGboXfVnKhmk6Dv'
openai.api_key = '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'

title = '모자 가게'
contents = '귀여운 비니, 시크한 캡모자, 힙한 벙거지'
summary = '겨울, 패션'
image = 'hat.jpg'

def generate_ad_menets(product_name, product_description, product_image):

  # 모델 - GPT 3.5 Turbo 선택
  model = "gpt-3.5-turbo"

  # 질문 작성하기
  query = f"상품 이름: {product_name}\n상품 내용: {product_description}\n상품 이미지: {product_image}\n추천 광고 멘트 3가지:"

  # 메시지 설정하기
  messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": query}
  ]

  # ChatGPT API 호출하기
  response = openai.ChatCompletion.create(
      model=model,
      messages=messages
  )
  answer = response['choices'][0]['message']['content']
  return answer


# 상품 정보 입력
# product_name = input("상품 이름을 입력하세요: ")
# product_description = input("상품 내용을 입력하세요: ")
# product_image = input("상품 이미지를 입력하세요: ")

# 상품 정보 입력
product_name = title
product_description = summary
product_image = image

  
# streamlit 광고하마 광고추천 페이지 기본설정
import streamlit as st
st.set_page_config(page_icon="🦛", page_title="광고하마 추천페이지", layout="wide")
st.subheader("사장님의 하나뿐인 마케터,")
st.header("광고하마입니다. 🦛")  
  
# 광고 멘트 생성 및 출력
# ad_menets = generate_ad_menets(product_name, product_description, product_image)
# print(f"추천 광고 멘트 3가지:\n{ad_menets}\n")
if st.button("광고 멘트 추천 받기"):
  text = generate_ad_menets(product_name, product_description, product_image)
  options = [s.split('. ')[1] for s in text.split('\n') if s]
  ment = st.radio("gpt가 추천하는 멘트 세가지 중 하나를 골라주세요.", options)
  st.write(ment)