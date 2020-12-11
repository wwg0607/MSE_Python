#!/usr/bin/env python
# coding: utf-8

# In[1]:


date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]            # 두 리스트를 딕셔너리로
close_table = dict(zip(date, close_price))           # 딕셔너리 생성을 위해 close table이라는 변수를 설정한 후 date와 close_price를 딕셔너리로 바꿔줌
print(close_table)

