import pandas as pd

from ta.trend import SMAIndicator, EMAIndicator, MACD, ADXIndicator, IchimokuIndicator, CCIIndicator, AroonIndicator

import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt

from utils.config import *

from utils import *
from utils.basic import create_dataframe
from utils.cross_line import cross_line_bearish, cross_line_bullish, cross_line_from_above, cross_line_from_bottom
from utils.cross_value import cross_value_from_above, cross_value_from_bottom
from utils.difference_from_line import difference_from_line
from utils.difference_from_value import difference_from_value
from utils.sum_in_period import *
from utils.up_down import up_down_line



def macd(df):
    macd_value = MACD(df[CLOSE_COLUMN], fillna=0)

    value_cross_0_above = cross_value_from_above(macd_value.macd(), 0)
    value_cross_0_bottom = cross_value_from_bottom(macd_value.macd(), 0)

    signal_cross_0_above = cross_value_from_above(macd_value.macd_signal(), 0)
    signal_cross_0_bottom = cross_value_from_bottom(macd_value.macd_signal(), 0)

    value_top_signal = up_down_line(macd_value.macd(), macd_value.macd_signal())
    signal_top_value = up_down_line(macd_value.macd_signal(), macd_value.macd())

    cross_signal_bullish = cross_line_bullish(macd_value.macd(), macd_value.macd_signal())
    cross_signal_bearish = cross_line_bearish(macd_value.macd(), macd_value.macd_signal())
    d = {
        'macd_value': macd_value.macd(),
        'macd_signal': macd_value.macd_signal(),
        'macd_value_cross_0_above': value_cross_0_above,
        'macd_value_cross_0_bottom': value_cross_0_bottom,
        'macd_signal_cross_0_above': signal_cross_0_above,
        'macd_signal_cross_0_bottom': signal_cross_0_bottom,
        'macd_value_top_signal': value_top_signal,
        'macd_signal_top_value': signal_top_value,
        'macd_cross_signal_bullish': cross_signal_bullish,
        'macd_cross_signal_bearish': cross_signal_bearish,
    }

    return create_dataframe(d)