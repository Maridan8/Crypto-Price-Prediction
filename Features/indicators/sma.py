import pandas as pd
from ta.trend import SMAIndicator

from utils.config import *
from utils.basic import create_dataframe
from utils.difference_from_line import over_line

def sma(df):
    sma_value_9 = SMAIndicator(df[CLOSE_COLUMN], 9, fillna = True).sma_indicator()
    price_over_sma = over_line(df[CLOSE_COLUMN], sma_value_9) #for long position

    # sma_value_5 = SMAIndicator(df[CLOSE_COLUMN], 5, fillna = True).sma_indicator()
    # sma_value_10 = SMAIndicator(df[CLOSE_COLUMN], 10, fillna = True).sma_indicator()
    # sma_value_20 = SMAIndicator(df[CLOSE_COLUMN], 20, fillna = True).sma_indicator()
    # sma_value_50 = SMAIndicator(df[CLOSE_COLUMN], 50, fillna = True).sma_indicator()
    # sma_value_100 = SMAIndicator(df[CLOSE_COLUMN], 100, fillna = True).sma_indicator()
    # sma_value_200 = SMAIndicator(df[CLOSE_COLUMN], 200, fillna = True).sma_indicator()

    # diff_from_price = difference_from_line(sma_value_5, df[CLOSE_COLUMN])
    # cross_line_bullish_5_10 = cross_line_bullish(sma_value_5, sma_value_10)
    # cross_line_bearish_5_10 = cross_line_bearish(sma_value_5, sma_value_10)

    # cross_line_bullish_5_20 = cross_line_bullish(sma_value_5, sma_value_20)
    # cross_line_bearish_5_20 = cross_line_bearish(sma_value_5, sma_value_20)

    # cross_line_bullish_5_50 = cross_line_bullish(sma_value_5, sma_value_50)
    # cross_line_bearish_5_50 = cross_line_bearish(sma_value_5, sma_value_50)

    # cross_line_bullish_5_100 = cross_line_bullish(sma_value_5, sma_value_100)
    # cross_line_bearish_5_100 = cross_line_bearish(sma_value_5, sma_value_100)

    d = {
        'sma_value_9': sma_value_9,
        'price_over_sma': price_over_sma,
        # 'sma_diff_from_price': diff_from_price,
        # 'sma_cross_line_bullish_5_10': cross_line_bullish_5_10,
        # 'sma_cross_line_bearish_5_10': cross_line_bearish_5_10,
        # 'sma_cross_line_bullish_5_20': cross_line_bullish_5_20,
        # 'sma_cross_line_bearish_5_20': cross_line_bearish_5_20,
        # 'sma_cross_line_bullish_5_50': cross_line_bullish_5_50,
        # 'sma_cross_line_bearish_5_50': cross_line_bearish_5_50,
        # 'sma_cross_line_bullish_5_100': cross_line_bullish_5_100,
        # 'sma_cross_line_bearish_5_100': cross_line_bearish_5_100,
    }

    return create_dataframe(d)