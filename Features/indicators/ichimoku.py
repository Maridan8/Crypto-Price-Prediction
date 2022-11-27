import pandas as pd
from ta.trend import IchimokuIndicator

from utils.config import *
from utils.basic import create_dataframe
from utils.difference_from_line import over_line

def cloud_color_detection(close, span_A, span_B):
    color = [0] * len(close)
    for i in range(len(close)):
        if ((close[i] > span_B[i]) and (close[i] > span_A[i])):
            color[i] = 1 #above kumo
        elif((close[i] < span_B[i]) and (close[i] < span_A[i])):
            color[i] = -1 #under kumo

    return color

def ichimoku(df):
    ichimoku_value = IchimokuIndicator(df[HIGH_COLUMN], df[LOW_COLUMN], fillna = True)
    tenkan_sen = ichimoku_value.ichimoku_conversion_line()
    kijun_sen = ichimoku_value.ichimoku_base_line()
    span_a = ichimoku_value.ichimoku_a()
    span_b = ichimoku_value.ichimoku_b()
    
    tenkan_over_kijun = over_line(tenkan_sen, kijun_sen) #for long position
    spanaA_over_spanB = over_line(span_b, span_a) #for long position
    
    # diff_tenkan_sen_with_close = difference_from_line(ichimoku_value.ichimoku_conversion_line(), df[CLOSE_COLUMN])
    # diff_kijun_sen_with_close = difference_from_line(ichimoku_value.ichimoku_base_line(), df[CLOSE_COLUMN])
    # diff_span_A_with_close = difference_from_line(ichimoku_value.ichimoku_a(), df[CLOSE_COLUMN])
    # diff_span_B_with_close = difference_from_line(ichimoku_value.ichimoku_b(), df[CLOSE_COLUMN])
    # diff_span_A_with_span_B = difference_from_line(ichimoku_value.ichimoku_a(), ichimoku_value.ichimoku_b())
    # diff_tenkan_with_kijun = difference_from_line(ichimoku_value.ichimoku_conversion_line(), ichimoku_value.ichimoku_base_line())
    # tenkan_cross_kijun = cross_line_from_above(ichimoku_value.ichimoku_conversion_line(), ichimoku_value.ichimoku_base_line())
    # kijun_cross_tenkan = cross_line_from_bottom(ichimoku_value.ichimoku_base_line(), ichimoku_value.ichimoku_conversion_line())

    cloud_color = cloud_color_detection(df[CLOSE_COLUMN], ichimoku_value.ichimoku_a(), ichimoku_value.ichimoku_b())
    
    d = {
        'ichimoku_span_A': span_a,
        'ichimoku_span_B':  span_b,
        'ichimoku_tenkan_sen': tenkan_sen,
        'ichimoku_kijun_sen': kijun_sen,
        'tenkan_over_kijun': tenkan_over_kijun,
        'spanaA_over_spanB': spanaA_over_spanB, 
        'ichimoku_price_in_cloud_color': cloud_color,
        # 'ichimoku_diff_span_A_with_close':  diff_span_A_with_close,
        # 'ichimoku_diff_span_B_with_close':  diff_span_B_with_close,
        # 'ichimoku_diff_tenkan_sen_with_close':  diff_tenkan_sen_with_close,
        # 'ichimoku_diff_kijun_sen_with_close':  diff_kijun_sen_with_close,
        # 'ichimoku_diff_span_A_with_span_B':  diff_span_A_with_span_B,
        # 'ichimoku_diff_tenkan_with_kijun':  diff_tenkan_with_kijun,
        # 'ichimoku_tenkan_cross_kijun':  tenkan_cross_kijun,
        # 'ichimoku_kijun_cross_tenkan':  kijun_cross_tenkan,
    }

    return create_dataframe(d)