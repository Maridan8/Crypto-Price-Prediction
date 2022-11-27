from ta.trend import SMAIndicator, EMAIndicator, MACD, ADXIndicator, IchimokuIndicator, CCIIndicator, AroonIndicator
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt
from utils.config import *

from utils import *
from utils.basic import create_dataframe
from utils.cross_line import cross_line_from_above, cross_line_from_bottom
from utils.cross_value import cross_value_from_above, cross_value_from_bottom
from utils.difference_from_line import difference_from_line
from utils.difference_from_value import difference_from_value
from utils.sum_in_period import *
from utils.up_down import up_down_line



def aroon(df):
    aroon_value = AroonIndicator(df[CLOSE_COLUMN], fillna=True)

    diff_from_up = difference_from_value(df[CLOSE_COLUMN], 100)
    diff_from_down = difference_from_value(df[CLOSE_COLUMN], 0)

    up_cross_70 = cross_value_from_bottom(aroon_value.aroon_up(), value=70)
    down_cross_70 = cross_value_from_above(aroon_value.aroon_down(), value=70)

    up_cross_down_above = cross_line_from_above(aroon_value.aroon_up(), aroon_value.aroon_down())
    up_cross_down_below = cross_line_from_bottom(aroon_value.aroon_up(), aroon_value.aroon_down())

    up_top_down = up_down_line(aroon_value.aroon_up(), aroon_value.aroon_down())
    down_top_up = up_down_line(aroon_value.aroon_down(), aroon_value.aroon_up())

    d = {
        'aroon_value': aroon_value.aroon_indicator(),
        'aroon_up_value': aroon_value.aroon_up(),
        'aroon_down_value': aroon_value.aroon_down(),
        'aroon_up_cross_70': up_cross_70,
        'aroon_down_cross_70': down_cross_70,
        'aroon_diff_from_up': diff_from_up,
        'aroon_diff_from_down': diff_from_down,
        'aroon_up_cross_down_above': up_cross_down_above,
        'aroon_up_cross_down_below': up_cross_down_below,
        'aroon_up_top_down': up_top_down,
        'aroon_down_top_up': down_top_up,
    }

    return create_dataframe(d)