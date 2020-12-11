#!/usr/bin/env python
# coding: utf-8

# In[7]:


def print_max(a, b, c) :        # 사용자 정의함수 print_max(a,b,c)
    max_val = 0
    if a > max_val :            # 0보다 클경우 a가 max_val
        max_val = a
    if b > max_val :            # max_val에 해당값 (a or 0)보다 클경우 b가 max_val
        max_val = b
    if c > max_val :            # c도 위와 마찬가지
        max_val = c
    print(max_val)              # 따라서 제일 큰값이 위함수들을 통해 계산될것이다.
# ex)
print_max(1,2,3)


# In[8]:


# OR

def print_max(a, b, c) :
    if a > b and a > c:             # 논리 연산자와 if 문을 통해 가장 큰 값 출력
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)
print_max(1,2,3)

