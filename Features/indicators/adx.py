import pandas as pd
from ta.momentum import RSIIndicator, StochRSIIndicator, WilliamsRIndicator, AwesomeOscillatorIndicator
from ta.volume import MFIIndicator, OnBalanceVolumeIndicator
from ta.trend import SMAIndicator, EMAIndicator, MACD, ADXIndicator, IchimokuIndicator, CCIIndicator, AroonIndicator
from ta.volatility import BollingerBands
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt

from utils import *
from utils.basic import create_dataframe
from utils.config import PERIOD
from utils.cross_line import cross_line_from_above, cross_line_from_bottom
from utils.cross_value import cross_value_from_above, cross_value_from_bottom
from utils.difference_from_line import difference_from_line
from utils.difference_from_value import difference_from_value
from utils.sum_in_period import *
from utils.trending import trend_down, trend_up
from utils.up_down import up_down_line
from utils.config import *


def adx(df):

    adx_value = ADXIndicator(df[HIGH_COLUMN], df[LOW_COLUMN], df[CLOSE_COLUMN], window=11, fillna=True)

    diff_DI_pos_from_neg = difference_from_line(adx_value.adx_pos(), adx_value.adx_neg())
    diff_from_down = difference_from_value(df[CLOSE_COLUMN], 0)

    DI_pos_cross_neg_above = cross_line_from_above(adx_value.adx_pos(), adx_value.adx_neg())
    DI_pos_cross_neg_bottom = cross_line_from_bottom(adx_value.adx_pos(), adx_value.adx_neg())

    DI_pos_top_neg = up_down_line(adx_value.adx_pos(), adx_value.adx_neg())
    DI_neg_top_pos = up_down_line(adx_value.adx_neg(), adx_value.adx_pos())

    trending_up = trend_up(adx_value.adx(), period=PERIOD)
    trending_down = trend_down(adx_value.adx(), period=PERIOD)

    d = {
        'adx_value': adx_value.adx(),
        'adx_DI_pos': adx_value.adx_pos(),
        'adx_DI_neg': adx_value.adx_neg(),
        'adx_diff_DI_pos_from_neg': diff_DI_pos_from_neg,
        'adx_diff_from_down': diff_from_down,
        'adx_DI_pos_cross_neg_above': DI_pos_cross_neg_above,
        'adx_DI_pos_cross_neg_bottom': DI_pos_cross_neg_bottom,
        'adx_DI_pos_top_neg': DI_pos_top_neg,
        'adx_DI_neg_top_pos': DI_neg_top_pos,
        'adx_trending_up': trending_up,
        'adx_trending_down': trending_down
    }

    return create_dataframe(d)