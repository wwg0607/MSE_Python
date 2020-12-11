#!/usr/bin/env python
# coding: utf-8

# In[1]:


리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']       # 리스트 안의 문자열 > 파일 이름
for 변수 in 리스트:                      # for 문을 사용해서 확장자가 h 또는 c 인 파일만을 출력
  split = 변수.split(".")                # 이를 위해 split을 통해 리스트 안의 파일명들을 .을 기준으로 나뉘게 함
  if (split[1] == "h") or (split[1] == "c"):       # 논리연산자 or 을 이용해서 split 했을경우 두번째에 h 또는 c 인 값들만을 골라냄
    print(변수)                             # 이 파일들을 모두 출력

