import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import talib
from keras.callbacks import TensorBoard
from sklearn.preprocessing import MinMaxScaler
ts.set_token('457a66c9299e50e9e0b2bf6c2f122bb24d560735f01b443158d1c85e')
# 日线接口
pro = ts.pro_api()
# df = pro.daily(ts_code='000001.SH', start_date='20100701', end_date='20190923')
df = ts.pro_bar(ts_code='000001.SH', asset='I', start_date='20100701', end_date='20190923')


df['trade_date'] = pd.to_datetime(df['trade_date'])
df.set_index('trade_date', inplace=True)


def create_dataset(dataset, look_back=7, foresight=3):
    X, Y = [], []
    for i in range(len(dataset)-look_back-foresight):
        obs = dataset[i:(i+look_back), 0] # Sequence of 7 stock prices as features forming an observation
       # Append sequence
        X.append(obs)
       # Append stock price value occurring 4 time-steps into future
        Y.append(dataset[i + (look_back+foresight), 0])
    return np.array(X), np.array(Y)
