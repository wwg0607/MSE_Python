#!/usr/bin/env python
# coding: utf-8

# In[8]:


def 함수0(num) :                 # 원소에 2를 곱하는 함수
    return num * 2

def 함수1(num) :                # 원소에 2를 더한다음 함수0 반복
    return 함수0(num + 2)

def 함수2(num) :                # 10을 더한후 함수1 반복
    num = num + 10
    return 함수1(num)

c = 함수2(2)                    # 따라서 ((2+10)+2)*2
print(c)

