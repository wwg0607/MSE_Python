#!/usr/bin/env python
# coding: utf-8

# In[3]:


리스트 = ["가", "나", "다", "라"]   # 4개의 문자열
# 이를 라 다 나 가 순서대로 출력 ( 거꾸로 )

for 변수 in 리스트[: :-1]:           # 반대로 하기위해 범위는 리스트의 전체 범위로 지정하고 증감폭을 음수로 설정한다
  print(변수)

