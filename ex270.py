#!/usr/bin/env python
# coding: utf-8

# In[13]:


class Stock:
    def __init__(self, name, code, per, pbr, 배당수익률):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code   
# 생성자에서 종목명, 종목코드, PER, PBR, 배당수익률을 입력받을 수 있도록 생성자 수정


# In[19]:


class Stock:
    def __init__(self, name, code, per, pbr, dividend):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend = dividend

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code

    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend):
        self.dividend = dividend
        
# PER, PBR, 배당수익률은 변경될 수 있는 값이므로 이 값을 변경할 때 사용하는 set_per, set_pbr, set_dividend 메서드를 추가해야 함
# 이 두가지를 실행해야 다음 값 진행가능


# In[20]:


종목 = []       # 종목이란 변수를 리스트로 설정

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)    # 종목명, 종목코드, PER, PBR, 배당수익률 순서대로 튜플생성

종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)      # 종목에 위 튜플을 추가

for i in 종목:          # 종목을 반복하여 돌면서 code, per을 출력하도록 함
    print(i.code, i.per)        # i >> Stock 클래스의 객체를 바인딩

