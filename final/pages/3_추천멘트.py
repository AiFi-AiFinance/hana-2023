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

# 광고 멘트 생성 및 출력
# ad_menets = generate_ad_menets(product_name, product_description, product_image)
# print(f"추천 광고 멘트 3가지:\n{ad_menets}\n")