import pandas as pd

from ta.volatility import BollingerBands
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt
from utils.config import *

from utils import *
from utils.basic import create_dataframe
from utils.config import PERIOD
from utils.cross_line import cross_line_bearish, cross_line_bullish
from utils.cross_value import cross_value_from_above, cross_value_from_bottom
from utils.difference_from_line import difference_from_line
from utils.sum_in_period import *

def band_expanding_tightening(upper, lower, period):
    result = [0] * len(upper)
    for i in range(period, len(upper)):
        cnt = 0
        for j in range(1, period):
            if ((upper[i-j] - lower[i-j]) < (upper[i] - lower[i])):
                cnt += 1
        
        if (cnt > (period/2)+1):
            result[i] = 1
        else:
            result[i] = -1
    return result


def bb(df):
    bb_value = BollingerBands(df[CLOSE_COLUMN], fillna=0)

    diff_from_upper_band = difference_from_line(df[CLOSE_COLUMN], bb_value.bollinger_hband())
    diff_from_lower_band = difference_from_line(df[CLOSE_COLUMN], bb_value.bollinger_lband())

    diff_from_lower_band = difference_from_line(df[CLOSE_COLUMN], bb_value.bollinger_lband())
    diff_from_lower_band = difference_from_line(df[CLOSE_COLUMN], bb_value.bollinger_lband())

    band_state = band_expanding_tightening(bb_value.bollinger_hband(), bb_value.bollinger_lband(), period=PERIOD)

    price_cross_upper_band_bullish = cross_line_bullish(df[CLOSE_COLUMN], bb_value.bollinger_hband())
    price_cross_lower_band_bearish = cross_line_bearish(df[CLOSE_COLUMN], bb_value.bollinger_hband())

    d = {
        'bb_upper_value': bb_value.bollinger_hband(),
        'bb_lower_value': bb_value.bollinger_lband(),
        'bb_diff_from_upper_band': diff_from_upper_band,
        'bb_diff_from_lower_band': diff_from_lower_band,
        'bb_band_state': band_state,
        'bb_price_cross_upper_band_bullish': price_cross_upper_band_bullish,
        'bb_price_cross_lower_band_bearish': price_cross_lower_band_bearish,
    }
    
    return create_dataframe(d)