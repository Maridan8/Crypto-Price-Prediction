import numpy as np
from utils.config import *

def is_support(df, i):  
  cond1 = df[LOW_COLUMN][i] < df[LOW_COLUMN][i-1]   
  cond2 = df[LOW_COLUMN][i] < df[LOW_COLUMN][i+1]   
  cond3 = df[LOW_COLUMN][i+1] < df[LOW_COLUMN][i+2]   
  cond4 = df[LOW_COLUMN][i-1] < df[LOW_COLUMN][i-2]  
  return (cond1 and cond2 and cond3 and cond4)
def is_resistance(df,i):  
  cond1 = df[HIGH_COLUMN][i] > df[HIGH_COLUMN][i-1]   
  cond2 = df[HIGH_COLUMN][i] > df[HIGH_COLUMN][i+1]   
  cond3 = df[HIGH_COLUMN][i+1] > df[HIGH_COLUMN][i+2]   
  cond4 = df[HIGH_COLUMN][i-1] > df[HIGH_COLUMN][i-2]  
  return (cond1 and cond2 and cond3 and cond4)
def is_far_from_level(value, levels, df):    
  ave =  np.mean(df[HIGH_COLUMN] - df[LOW_COLUMN])    
  return np.sum([abs(value-level)<ave for _,level in levels])==0

def find_SR(closePrice, period):
    sr = []
    for i in range(period, len(closePrice)-period):
        if closePrice[i] >= max(closePrice[i-period:i+period]) or closePrice[i] <= min(closePrice[i-period:i+period]):
            sr.append(closePrice[i])
    return sr



def find_support_resistance_levels(df):
    levels = []
    for i in range(2, len(df)-2):  
        if is_support(df, i):    
            low = df[LOW_COLUMN][i]
            if is_far_from_level(low, levels, df):      
                levels.append((i, low))  
        elif is_resistance(df, i):    
            high = df[HIGH_COLUMN][i]    
            if is_far_from_level(high, levels, df):      
                levels.append((i, high))
    
    return levels
                
def min_support(c, levels):
    min = levels[0][1] - c
    for i in range(len(levels)):
        if ((levels[i][1] - c) > 0 & ((levels[i][1] - c) < min)):
            min = (levels[i][1] - c)  

    return min
def min_resistance(c, levels):
  min = c - levels[0][1]
  for i in range(len(levels)):
    if ((c - levels[i][1]) > 0 & ((c - levels[i][1]) < min)):
      min = (c - levels[i][1])  

  return min

