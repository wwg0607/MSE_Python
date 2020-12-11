#!/usr/bin/env python
# coding: utf-8

# In[2]:


low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
# 130 번 문제와 마찬가지로 고가와 저가의 차 >> 변동폭
volatility = []                  # 리스트 생성
for i in range(len(low_prices)) :           # 저가의 값의 개수 범위안에서 for문이 반복
    volatility.append(high_prices[i] - low_prices[i])       # 둘의 차를 위 리스트에 저장

