def cross_value_from_bottom(column, value):
  crossed = [0] * len(column)
  for i in range(1, len(column)):
    if((column[i] >= value) and (column[i-1] < value)):
      crossed[i] = 1

  return crossed

def cross_value_from_above(column, value):
  crossed = [0] * len(column)
  for i in range(1, len(column)):
    if((column[i] <= value) and (column[i-1] > value)):
      crossed[i] = 1

  return crossed