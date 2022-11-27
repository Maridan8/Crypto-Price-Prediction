import pandas as pd

from ta.trend import SMAIndicator, EMAIndicator, MACD, ADXIndicator, IchimokuIndicator, CCIIndicator, AroonIndicator

import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt
from utils.config import *

from utils import *
from utils.basic import create_dataframe
from utils.cross_line import cross_line_bearish, cross_line_bullish
from utils.cross_value import cross_value_from_above, cross_value_from_bottom
from utils.difference_from_line import difference_from_line
from utils.sum_in_period import *

def ema(df):
    ema_value_5 = EMAIndicator(df[CLOSE_COLUMN], 5, fillna=True).ema_indicator()
    ema_value_10 = EMAIndicator(df[CLOSE_COLUMN], 10, fillna=True).ema_indicator()
    ema_value_20 = EMAIndicator(df[CLOSE_COLUMN], 20, fillna=True).ema_indicator()
    ema_value_50 = EMAIndicator(df[CLOSE_COLUMN], 50, fillna=True).ema_indicator()
    ema_value_100 = EMAIndicator(df[CLOSE_COLUMN], 100, fillna=True).ema_indicator()

    diff_from_price = difference_from_line(ema_value_5, df[CLOSE_COLUMN])
    cross_line_bullish_5_10 = cross_line_bullish(ema_value_5, ema_value_10)
    cross_line_bearish_5_10 = cross_line_bearish(ema_value_5, ema_value_10)

    cross_line_bullish_5_20 = cross_line_bullish(ema_value_5, ema_value_20)
    cross_line_bearish_5_20 = cross_line_bearish(ema_value_5, ema_value_20)

    cross_line_bullish_5_50 = cross_line_bullish(ema_value_5, ema_value_50)
    cross_line_bearish_5_50 = cross_line_bearish(ema_value_5, ema_value_50)

    cross_line_bullish_5_100 = cross_line_bullish(ema_value_5, ema_value_100)
    cross_line_bearish_5_100 = cross_line_bearish(ema_value_5, ema_value_100)

    d = {
        'ema_value_5': ema_value_5,
        'ema_diff_from_price_percent': diff_from_price,
        'ema_cross_line_bullish_5_10': cross_line_bullish_5_10,
        'ema_cross_line_bearish_5_10': cross_line_bearish_5_10,
        'ema_cross_line_bullish_5_20': cross_line_bullish_5_20,
        'ema_cross_line_bearish_5_20': cross_line_bearish_5_20,
        'ema_cross_line_bullish_5_50': cross_line_bullish_5_50,
        'ema_cross_line_bearish_5_50': cross_line_bearish_5_50,
        'ema_cross_line_bullish_5_100': cross_line_bullish_5_100,
        'ema_cross_line_bearish_5_100': cross_line_bearish_5_100,
    }

    return create_dataframe(d)