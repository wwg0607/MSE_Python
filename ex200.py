#!/usr/bin/env python
# coding: utf-8

# In[5]:


ohlc = [["open", "high", "low", "close"],          # ohlc 데이터
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
profit = 0                                  # 0에 더해야 모두 더해진 총 수익금이 나옴
for row in ohlc[1:]:                        # 데이터 값중 첫번째인 ["open", "high", "low", "close"]제외
    profit += (row[3] - row[0])             # 나머지 값들 중 마지막값에서 첫값을 뺌

