import pandas as pd
from ta.trend import PSARIndicator

from utils.config import *
from utils.basic import create_dataframe
from utils.difference_from_line import under_line, over_line

def pSar(df):
    pSar_value = PSARIndicator(df[HIGH_COLUMN], df[LOW_COLUMN], df[CLOSE_COLUMN], fillna = True).psar()
    
    # price_under_pSar = under_line(df[CLOSE_COLUMN], pSar_value)
    price_over_pSar = over_line(df[CLOSE_COLUMN], pSar_value) #for long position

    d = {
        'pSar_value': pSar_value,
        'price_over_pSar': price_over_pSar,  
    }

    return create_dataframe(d)
    