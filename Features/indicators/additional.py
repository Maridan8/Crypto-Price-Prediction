import pandas as pd

from ta.volume import MFIIndicator, OnBalanceVolumeIndicator

import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt


from utils import *
from utils.basic import create_dataframe
from utils.config import *
from utils.sum_in_period import *

# def additional(df):
    # obv_value = ta.obv(df[CLOSE_COLUMN], df[VOLUME_COLUMN])
    # rvi_value = ta.rvi(df[HIGH_COLUMN], df[LOW_COLUMN], df[CLOSE_COLUMN])

    # d = {
    #     'obv_value': obv_value,
    #     'rvi_value': rvi_value,
    # }

    # return create_dataframe(d)