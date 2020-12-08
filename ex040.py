#!/usr/bin/env python
# coding: utf-8

# In[1]:


data = "   삼성전자   "     # 좌우에 공백 존재
data1 = data.strip()        # 공백을 제거하기위해 strip 사용 >> 이로 인해 원본 문자열은 그래도 유지되고 좌우의 공백만 제거 가능
print(data1)                # 제거된 자료형이 출력됨

