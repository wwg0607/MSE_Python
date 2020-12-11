#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1~10 을 모두 곱한 값 - for 문 사용

result = 1             # result를 0으로 설정할 경우 무엇을 곱하든 값이 0이됨
for i in range(1, 11) :        # 1부터 10까지의 수들이 for 문을 반복
    result *= i            # += 기호와 비슷 # result = result*i 축약
print(result)

