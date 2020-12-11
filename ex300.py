#!/usr/bin/env python
# coding: utf-8

# try:
#     실행 코드
#     
# except:
#     예외가 발생했을 때 수행할 코드
#     
# else:
#     예외가 발생하지 않았을 때 수행할 코드
#     
# finally:
#     예외 발생 여부와 상관없이 항상 수행할 코드

# In[2]:


per = ["10.31", "", "8.00"]

for i in per:
#    print(float(per))
# 위 주석이 포함된 코드에 예외처리 사용
# try, except, else, finally에 적당한 코드 작성
    try:
        print(float(i))           # print(float(per))을 실행하는 코드
    except:
        print(0)                 # 에외 발생시 0이 생성되도록 하는 코드
    else:              
        print("clean data")         # 예외가 발생하지 않았을 경우 clean data라는 값이 출력되도록 하는 코드
    finally:
        print("변환 완료")           # 예외 발생 여부와 관계없이 항상 수행되는 코드 (무조건 출력)
# 따라서 10.31 >> 예외 발생 x 10.31 clean data 변환 완료 출력
# 공백 >> 예외 >> 0 변환완료 출력
# 8.0 >> 10.31과 동일

