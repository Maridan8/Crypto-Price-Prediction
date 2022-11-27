
def difference_from_line(column, line):
    diff = [0] * len(column)
    for i in range(len(column)):
        diff[i] = (column[i] - line[i]) / 100
    
    return diff

def under_line(column, line):
    diff = [0] * len(column)

    for i in range(len(column)):
        if column[i] < line[i]:
            diff[i] = 1
    
    return diff

def over_line(column, line):
    diff = [0] * len(column)

    for i in range(len(column)):
        if column[i] > line[i]:
            diff[i] = 1
    
    return diff