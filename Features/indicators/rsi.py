import pandas as pd
import matplotlib.pyplot as plt
from ta.volume import MFIIndicator, OnBalanceVolumeIndicator
from ta.momentum import RSIIndicator, StochRSIIndicator, WilliamsRIndicator, AwesomeOscillatorIndicator

from utils import *
from utils.config import *
from utils.config import PERIOD
from utils.basic import create_dataframe
from utils.trending import trend_down, trend_up
from utils.difference_from_value import under_value, over_value
from utils.cross_value import cross_value_from_above, cross_value_from_bottom

def count_above_candle(l, period, value):
    counts = [0] * len(l)
    for i in range(period, len(l)):
        count = 0
        for j in range(i-period, i):
            if l[j] > value:
                count += 1
        counts[i] = count

    return counts

def count_bellow_candle(l, period, value):
    counts = [0] * len(l)
    for i in range(period, len(l)):
        count = 0
        for j in range(i-period, i):
            if l[j] < value:
                count += 1
        counts[i] = count

    return counts

def rsi(df):
    rsi_value = RSIIndicator(df[CLOSE_COLUMN], fillna = True).rsi()

    under_20 = under_value(rsi_value, value = 20)
    over_80 = over_value(rsi_value, value = 80)

    # cross_80 = cross_value_from_bottom(rsi_value, value = 80)
    # cross_20 = cross_value_from_above(rsi_value, value = 20)

    # num_of_candle_above_80 = count_above_candle(rsi_value, period = PERIOD, value = 80)
    # num_of_candle_bellow_20 = count_bellow_candle(rsi_value, period=PERIOD, value = 20)

    # trending_up = trend_up(rsi_value, period = PERIOD)
    # trending_down = trend_down(rsi_value, period = PERIOD)

    d = {
        'rsi_value': rsi_value,
        'rsi_over_80': over_80,
        'rsi_under_20': under_20
        # 'rsi_crossed_80': cross_80,
        # 'rsi_crossed_20': cross_20,
        # 'rsi_num_of_candle_above_80': num_of_candle_above_80,
        # 'rsi_num_of_candle_bellow_20': num_of_candle_bellow_20,
        # 'rsi_trending_up': trending_up,
        # 'rsi_trending_down': trending_down
    }

    return create_dataframe(d)