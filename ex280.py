#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random


class Account:         # 클래스 변수 사용
    # class variable
    account_count = 0

# 입출금 내역 기록되도록 하는 코드

    def __init__(self, name, balance):       # self, name, balance 튜플 사용자 정의함수
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []            # 입출금 내역을 기록하기 위해 리스트 생성

        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count += 1 # Account 클래스로부터 생성된 계좌 객체의 개수 저장

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  # Account.account_count

    def deposit(self, amount):          # 예금을 할 때
        if amount >= 1:                 # 당연 금액은 1원 이상
            self.deposit_log.append(amount)      # 입금 시 내역을 리스트로 저장
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:         # 5, 10, 15
                # 이자 지금
                self.balance = (self.balance * 1.01)      # 1%의 이자


    def withdraw(self, amount):
        if self.balance > amount:
            self.withdraw_log.append(amount)       # 출금 시 내역을 리스트로 저장
            self.balance -= amount                # 출금 금액을 이전 잔액에서 제외시켜 현재 잔액을 생성

    def display_info(self):                # Account 인스턴스에 저장된 정보를 출력하도록 하는 메서드 ( 따라서 입출금내역을 기록하는 코드를 생성하는 지금은 불필요)
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

# 출금, 입금 내역을 기록하는 함수 (반복문 사용)

    def withdraw_history(self):
        for amount in self.withdraw_log:       # 출금 금액을 가져와서 출금하도록 함
            print(amount)

# 인덱스를 만들고자 하면 가능

    def deposit_history(self):
        for amount in self.deposit_log:      # 입금 금액도 마찬가지로 amount 프린트
            print(amount)


k = Account("Kim", 1000)            # 김씨가 천원을 넣음
k.deposit(100)                       # 예금 100,200,300원
k.deposit(200)
k.deposit(300)
k.deposit_history()                 # 메소드 호출
# 100,200,300 출력 완료

k.withdraw(100)        # 출금 100,200
k.withdraw(200)
k.withdraw_history()
# 100,200 출력완료

