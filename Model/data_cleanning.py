
import pandas as pd

def preprocess_data():
    # csv파일 열기
    df = pd.read_csv('../Data/hanacard_sample.csv')
    
    #필요 없는 특성 제거
    allColumns = df.columns
    params = ['기준년월','광역시도명','시군구명','읍면동명','당사업종대분류코드명','당사업종중분류코드명','당사업종코드','업종명','구분_개인법인','구분_연령','구분_성별','구분_직장','추정소득구간','신용등급구간','카드이용건수','카드이용금액']

    df = df.drop(allColumns.drop(params), axis=1)
    df = df.dropna()
    print(df)
    
preprocess_data()


    

    