#!/usr/bin/env python
# coding: utf-8

# In[1]:


fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}      # dic
user = input("좋아하는 과일은?")           # 한라봉을 입력할 경우 '오답입니다'가 나와야한다 (딕셔너리 값에 포함되어있지 않기 때문)
if user in fruit.values():            # 위 딕셔너리의 값에 존재할 경우 '정답입니다'
    print("정답입니다.")
else:                                 # 그 외 오답입니다
    print("오답입니다.")
    
    
# 따라서 한라봉을 입력할 경우 '오답입니다'가 출력됨을 확인 가능

