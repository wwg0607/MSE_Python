#!/usr/bin/env python
# coding: utf-8

# In[4]:


class OMG :                  # 클래스 OMG
    def print() :
        print("Oh my god")     # oh my god을 출력

myStock = OMG()
myStock.print()

# >> 밑과 같은 error 발생

TypeError Traceback (most recent call last)
<ipython-input-233-c85c04535b22> in <module>()
----> myStock.print()

TypeError: print() takes 0 positional arguments but 1 was given
    
# 이유

class OMG :
    def print() :
        print("Oh my god")


mystock = OMG()
mystock.print()      #mystock 안에 print x 따라서 OMG에 들어가서 함수를 호출해야함
# 그러나 객체하고 점을 찍으면 OMG.print(mystock) 이것과 같음
# 즉, 객체가 print()안으로 넘어간다 그러나 my stock이라는 것 존재 x >> error


# In[5]:


# 따라서 이렇게 진행해야함

class OMG :           
    def print(self) :                  # self를 꼭 추가해야함
        print("Oh my god")   
myStock = OMG()
myStock.print()

