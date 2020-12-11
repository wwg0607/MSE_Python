#!/usr/bin/env python
# coding: utf-8

# In[2]:


def message1():               # A를 출력하는 함수
    print("A")
    
def message2():               # B를 출력하는 함수
    print("B")

def message3():
    for i in range (3) :      # B를 출력하는 함수와 C 출력을 총 3번 반복
        message2()
        print("C")
    message1()                # 마지막에 A를 출력하는 함수

message3()                    # print 생략

