import pandas as pd

from ta.momentum import RSIIndicator, StochRSIIndicator, WilliamsRIndicator, AwesomeOscillatorIndicator

import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt


from utils.config import *

from utils import *
from utils.basic import create_dataframe
from utils.config import PERIOD
from utils.cross_value import cross_value_from_above, cross_value_from_bottom
from utils.sum_in_period import *
from utils.trending import trend_down, trend_up

def wr(df):
    wr_value = WilliamsRIndicator(df[HIGH_COLUMN], df[LOW_COLUMN], df[CLOSE_COLUMN], fillna=True).williams_r()

    cross_20_bottom = cross_value_from_bottom(wr_value, value=-20)
    cross_20_above = cross_value_from_above(wr_value, value=-20)
    cross_50_bottom = cross_value_from_bottom(wr_value, value=-50)
    cross_50_above = cross_value_from_above(wr_value, value=-50)
    cross_80_bottom = cross_value_from_bottom(wr_value, value=-80)
    cross_80_above = cross_value_from_above(wr_value, value=-80)

    positive_change_sum = sum_in_period_positive(wr_value, period=PERIOD)
    negative_change_sum = sum_in_period_negative(wr_value, period=PERIOD)

    trending_up = trend_up(wr_value, period=PERIOD)
    trending_down = trend_down(wr_value, period=PERIOD)
    d = {
        'wr_value': wr_value,
        'wr_cross_20_bottom': cross_20_bottom,
        'wr_cross_20_above': cross_20_above,
        'wr_cross_50_bottom': cross_50_bottom,
        'wr_cross_50_above': cross_50_above,
        'wr_cross_80_bottom': cross_80_bottom,
        'wr_cross_80_above': cross_80_above,
        'wr_positive_change_sum': positive_change_sum,
        'wr_negative_change_sum': negative_change_sum,
        'wr_trending_up': trending_up,
        'wr_trending_down': trending_down
    }

    return create_dataframe(d)