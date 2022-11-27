# if you pass (A, B), this function may calculate A>B, so pass inputs in order you want
def up_down_line(column, line):
  up_down = [0] * len(column)
  for i in range(len(column)):
    if column[i]>line[i]:
      up_down[i] = 1

  return up_down