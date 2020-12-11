#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 첫번째 방법
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()    # 리스트의 각원소들을 오름차순으로 정렬가능하게 해주는 함수 사용
print(data)


# In[2]:


# 두번째 방법
data = [2, 4, 3, 1, 5, 10, 9]
data2 = sorted(data)        # data2라는 새로운 변수를 만들어 그 변수에는 data의 원소들이 오름차순으로 존재하도록 함
print(data2)

