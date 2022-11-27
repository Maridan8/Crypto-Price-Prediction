from utils.config import WATCH_BACK_COLUMNS


def cross_line_from_bottom(column, line):
    crossed = [0] * len(column)
    for i in range(1, len(column)):
        if column[i-1] < line[i-1] and column[i] >= line[i]:
            crossed[i] = 1

    return crossed

def cross_line_from_above(column, line):
    crossed = [0] * len(column)
    for i in range(1, len(column)):
        if column[i-1] > line[i-1] and column[i] >= line[i]:
            crossed[i] = 1

    return crossed

def cross_line_bullish(column, line):
  crossed = [0] * len(column)
  for i in range(WATCH_BACK_COLUMNS, len(column)):
    if(column[i] >= line[i]):
      power_of_cross = 0
      for j in range(i-WATCH_BACK_COLUMNS, i):
        if(column[j] <= column[i]):
          power_of_cross += 1
      if( power_of_cross >= ((WATCH_BACK_COLUMNS/2)+1)):
        crossed[i] = 1
  
  return crossed

def cross_line_bearish(column, line):
  crossed = [0] * len(column)
  for i in range(WATCH_BACK_COLUMNS, len(column)):
    if(column[i] <= line[i]):
      power_of_cross = 0
      for j in range(i-WATCH_BACK_COLUMNS, i):
        if(column[j] >= column[i]):
          power_of_cross += 1
      if( power_of_cross >= ((WATCH_BACK_COLUMNS/2)+1)):
        crossed[i] = 1
  
  return crossed