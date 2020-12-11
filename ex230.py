#!/usr/bin/env python
# coding: utf-8

# In[2]:


def my_print (a, b) :          # 사용자 정의함수
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)            # 순서가 바뀌더라도 변수를 a, b를 위에서 설정하였기 때문에 변수에 맞는 값으로 대응하여 출력됨

