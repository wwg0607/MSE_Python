#!/usr/bin/env python
# coding: utf-8

# In[1]:


apart = [ [101, 102], [201, 202], [301, 302] ]     # 이 리스트의 값들 뒤에 각각 '호'라는 글자를 붙여 출력되도록
for row in apart:           # 아파트의 층들
    for col in row:         # 층 중에서 호
        print(col, "호")    # 호들 뒤에 '호'를 붙여 출력되도록함
print("-" * 5)              # 또한 이들 뒤 - 가 5번 출력되도록 함

