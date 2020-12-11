#!/usr/bin/env python
# coding: utf-8

# In[3]:


class 부모:            # 부모 class
    def __init__(self):  # 생성자
        print("부모생성")

class 자식(부모):   # 자식 class (부모 class 상속)
    def __init__(self):    # 생성자
        print("자식생성")
        super().__init__()  # super를 통해 부모 class 접근
                            # self는 알아서 전달됨

나 = 자식()     # 자식 class의 객체 생성
# 결과 예상 ;  자식 클래스의 객체 생성 >> 생성자 호출 >> 자식생성 프린트 >> 부모클래스에 접근 >> 부모생성 프린트

