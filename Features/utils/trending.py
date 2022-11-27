def trend_up(column, period):
  trend = [0]*period + [1] * (len(column)-period)
  for i in range(period, len(column)):
    if min(column[i-period:i+1]) < column[i-period]:
        trend[i] = 0
  return trend

def trend_down(column, period):
  trend = [0] * period + [1] * (len(column) - period)

  for i in range(period, len(column)):
    if max(column[i - period : i + 1]) > column[i - period]:
        trend[i] = 0

  return trend

def trend_neutral(trendUp, trendDown):
  trend = [0] * len(trendUp)
  for i in range(len(trendUp)):
    if trendUp[i] == 0 and trendDown[i] == 0:
      trend[i] = 1
  return trend