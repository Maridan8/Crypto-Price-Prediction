import pandas as pd
from ta.momentum import StochRSIIndicator

from utils.config import *
from utils.basic import create_dataframe
from utils.difference_from_value import under_value, over_value
from utils.cross_line import cross_line_bearish, cross_line_bullish

STOCH_D_DEFULT = 3
STOCH_K_DEFULT = 14

def stochRsi(df):
    stochRsi = StochRSIIndicator(df[CLOSE_COLUMN], fillna = True)
    stochRsi_value = stochRsi.stochrsi()
    stochRsi_K = stochRsi.stochrsi_k()
    stochRsi_D = stochRsi.stochrsi_d()
    
    under_20 = under_value(stochRsi_value, value = 20/100)
    over_80 = over_value(stochRsi_value, value = 80/100)

    K_cross_D_bullish = cross_line_bullish(stochRsi_K, stochRsi_D)
    K_cross_D_bearish = cross_line_bearish(stochRsi_K, stochRsi_D)
    
    # K_cross_20_above = cross_value_from_above(stoch_value.stochrsi_k(), 20)
    # K_cross_20_bottom = cross_value_from_bottom(stoch_value.stochrsi_k(), 20)
    # K_cross_50_above = cross_value_from_above(stoch_value.stochrsi_k(), 50)
    # K_cross_50_bottom = cross_value_from_bottom(stoch_value.stochrsi_k(), 50)
    # K_cross_80_above = cross_value_from_above(stoch_value.stochrsi_k(), 80)
    # K_cross_80_bottom = cross_value_from_bottom(stoch_value.stochrsi_k(), 80)

    # D_cross_20_above = cross_value_from_above(stoch_value.stochrsi_d(), 20)
    # D_cross_20_bottom = cross_value_from_bottom(stoch_value.stochrsi_d(), 20)
    # D_cross_50_above = cross_value_from_above(stoch_value.stochrsi_d(), 50)
    # D_cross_50_bottom = cross_value_from_bottom(stoch_value.stochrsi_d(), 50)
    # D_cross_80_above = cross_value_from_above(stoch_value.stochrsi_d(), 80)
    # D_cross_80_bottom = cross_value_from_bottom(stoch_value.stochrsi_d(), 80)

    d = {
        'stochRsi_value': stochRsi_value,
        'stoch_K_value': stochRsi_K,
        'stoch_D_value': stochRsi_D,
        'stoch_K_cross_D_bullish': K_cross_D_bullish,
        'stoch_K_cross_D_bearish': K_cross_D_bearish,
        'stochRsi_over_80': over_80,
        'stochRsi_under_20': under_20,  
        # 'stoch_K_cross_20_above':K_cross_20_above,
        # 'stoch_K_cross_20_bottom': K_cross_20_bottom,
        # 'stoch_K_cross_50_above':K_cross_50_above,
        # 'stoch_K_cross_50_bottom': K_cross_50_bottom,
        # 'stoch_K_cross_80_above':K_cross_80_above,
        # 'stoch_K_cross_80_bottom': K_cross_80_bottom,
        # 'stoch_D_cross_20_above':D_cross_20_above,
        # 'stoch_D_cross_20_bottom': D_cross_20_bottom,
        # 'stoch_D_cross_50_above':D_cross_50_above,
        # 'stoch_D_cross_50_bottom': D_cross_50_bottom,
        # 'stoch_D_cross_80_above':D_cross_80_above,
        # 'stoch_D_cross_80_bottom': D_cross_80_bottom,
    }

    return create_dataframe(d)
    