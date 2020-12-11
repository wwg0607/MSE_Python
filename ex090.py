#!/usr/bin/env python
# coding: utf-8

# In[2]:


icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
>> icecream['누가바']
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    icecream['누가바']
KeyError: '누가바'           #  >> error 발생 (because '누가바'라는 키는 딕셔너리에 존재 x)

