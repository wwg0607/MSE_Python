#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']      # 비트코인의 가격정보를 딕셔너리로 가져오는 코드
# 이 딕셔너리 안에 시가, 종가, 최고가,최저가 등 저장
# opening price : 시작 거래 금액
변동폭 = float(btc['max_price']) - float(btc['min_price']) # 이 중 최고가와 최저가의 차이를 변동폭으로 정의한다.
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가:      #  조건문을 활용하여 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장" 이 출력 되도록 함      
    print("상승장")
else:                           # 그 외의 경우 "하락장" 출력
    print("하락장")

