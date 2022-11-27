import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt

from utils.config import *

from utils import *
from utils.basic import create_dataframe
from utils.config import PERIOD
from utils.support_resistance import *


def in_levels(levels, j):
    for i in range(len(levels)):
        if(j == levels[i][0]):
            return True
    return False

def SR(df):
    # nearest_support = [0] * len(df[CLOSE_COLUMN])
    # nearest_resistance = [0] * len(df[CLOSE_COLUMN])
    # point = [0] * len(df[CLOSE_COLUMN])

    sr = find_SR(df[CLOSE_COLUMN], SHORT_TERM)
    distance_high_from_nearest_SR = []
    distance_low_from_nearest_SR = []
    distance_close_from_nearest_SR = []

    for i in range(len(df[CLOSE_COLUMN])):
        distance_high_from_nearest_SR.append(min(list(map(lambda x: abs(x - df.loc[i, HIGH_COLUMN]),sr))))
        distance_low_from_nearest_SR.append(min(list(map(lambda x: abs(x - df.loc[i, LOW_COLUMN]),sr))))
        distance_close_from_nearest_SR.append(min(list(map(lambda x: abs(x - df.loc[i, CLOSE_COLUMN]),sr))))


    # levels = find_support_resistance_levels(df)
    # for i in range(len(df[CLOSE_COLUMN])):
    #     nearest_support[i] = min_support(df[CLOSE_COLUMN][i], levels)
    #     nearest_resistance[i] = min_resistance(df[CLOSE_COLUMN][i], levels)
    
    # for i in range(len(df[CLOSE_COLUMN])):
    #     if in_levels(levels, i):
    #         point[i] = 1
    

    d = {
        # 'SR_point': point,
        # 'SR_nearest_support': nearest_support,
        # 'SR_nearest_resistance': nearest_resistance,
        'SR_distance_high_from_nearest_SR': distance_high_from_nearest_SR,
        'SR_distance_low_from_nearest_SR': distance_low_from_nearest_SR,
        'SR_distance_close_from_nearest_SR': distance_close_from_nearest_SR,
    }

    return create_dataframe(d)