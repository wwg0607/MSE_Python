#!/usr/bin/env python
# coding: utf-8

# In[4]:


data = "039490    "           # 오른쪽에 공백 존재
data = data.rstrip()          # 이를 제거하기 위해 rstrip을 사용해서 공백을 제거하고 나머지는 그대로 반환되도록 한다
print(data)

