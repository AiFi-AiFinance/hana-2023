import re
import pandas as pd

# 콜럼이름(데이터 예시, 특징, 형식)
# 기준년월(202001, YYYYMM, int): 전처리 필요 없음

# 광역시도명("서울", string)
# 시군구명("중구", string)
# 읍면동명("다동", string): 기상청이 쓰는 지역번호를 가져올까?

# 당사업종대분류코드명
# 당사업종중분류코드명
# 당사업종코드: 코드만 해석할 줄 알면 그대로 써도 좋을듯
# 업종명

# 구분_개인법인("개인", string): 원핫인코딩
# 구분_연령("30대", string): int값으로 변환
def age_to_int(data_string):
    if '대' in data_string:
        age = (int(data_string[0])*10) -5
    else:
        # 예외 처리를 하거나 None 값을 반환합니다.
        age = None
    return age
# 구분_성별("F", string): 원핫인코딩
# 구분_직장("기타소득자", string): 원핫인코딩

# 추정소득구간("5천만원미만", string): int값으로 변환
# 신용등급구간("1-3등급", string): int값으로 변환
# 문자열 데이터를 중앙값으로 변환하는 함수
def str_to_median(data_str):
    if '천만원미만' in data_str:
        value = int(data_str[0])
        median_value = (value -1) * 10000000

    elif '억원미만' in data_str:
        value = int(data_str[0])
        median_value = (value) * 1000000000 
        
    elif '억원이상' in data_str:
        value = int(data_str[0])
        median_value = (value +1) * 1000000000
        
    elif '-' in data_str:
        # 범위형 데이터인 경우
        # 문자열을 '-' 기준으로 분리하여 최소값과 최대값을 추출합니다.
        range_list = data_str.split('-')
        min_value = int(range_list[0])
        max_value = int(range_list[1][0])
        
        # 최소값과 최대값을 더한 후 2로 나누어 중앙값을 계산합니다.
        median_value = (min_value + max_value) / 2.0

    else:
        # 범위형, 이상형, 미만형 데이터가 아닌 경우
        # 예외 처리를 하거나 None 값을 반환합니다.
        median_value = None

    # 중앙값을 반환합니다.
    return median_value

# 카드이용건수(1, int): 음수 값은 drop
# 카드이용금액(6075, int): 음수 값은 drop