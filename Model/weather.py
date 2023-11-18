# 기상청 데이터 연결 "기상청_단기예보 ((구)_동네예보) 조회서비스"
import requests
import xml.etree.ElementTree as ET
from datetime import datetime
string = '날씨_'
key = '맑음'

# API 요청 URL
url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'

# 인증키
api_key = 'NminqLTNuSX5OFbyRamiOBFhuUBormib7/IeKYFKpWn1iXnxa1PEQ5IZAfJWebf8nOOb2FplMo5tdutaV6kUxQ=='

# 현재 날짜와 시간 가져오기
now = datetime.now()
date = now.strftime('%Y%m%d')  # 날짜 형식 변환
time = now.strftime('%H')+'00' # 시간 형식 변환  --> 여기서 오류, 10분 미만일 때 API 못불러옴

# # 사용자로부터 날짜와 시간 입력받기
# date = input('날짜를 입력하세요 (예: 20230608): ')
# time = input('시간을 입력하세요 (예: 1400): ')

# 요청 파라미터
params = {
    'serviceKey': api_key,
    'numOfRows': '10',  # 가져올 데이터 개수
    'dataType': 'XML',  # 응답 데이터 형식
    'base_date': date,  # 기준 날짜
    'base_time': time,  # 기준 시간
    'nx': '60',  # 위도
    'ny': '127'  # 경도
}

# API 요청 보내기
response = requests.get(url, params=params)
if (response.status_code != 200):
    params['base_time'] = '0000'
    response = requests.get(url, params=params)
xml_data = response.text

# XML 파싱
tree = ET.ElementTree(ET.fromstring(xml_data))
root = tree.getroot()

# 필요한 데이터 추출
items = root.findall('.//item')

found = False

for item in items:
    category = item.find('category').text
    if category == 'T1H':  # 기온(category=T1H) 데이터 추출
        temp = item.find('obsrValue').text
        found = True
    elif category == 'REH':  # 습도(category=REH) 데이터 추출
        humidity = item.find('obsrValue').text
        found = True
    elif category == "SKY": # 맑음=1, 흐림=4
        sky = item.find('obsrValue').text
        if sky == '4':
            key = '흐림'
        found = True
    elif category == "PTY": # 강설=3, 강우=1
        pty = item.find('obsrValue').text
        if pty == '3': 
            key = '강설'
        elif pty == '1':
            key = '강우'
        found = True
    elif category == "WSD": # 강풍>=9
        wsd = item.find('obsrValue').text 
        wsd = int(float(wsd))
        if wsd >= 9: 
            key = '강풍'
        found = True
      
if not found:
    print('해당 날짜와 시간에 대한 데이터를 찾을 수 없습니다.')
df.loc[string + key] = 1.0
df.loc['기온'] = temp
df.loc['습도'] = humidity