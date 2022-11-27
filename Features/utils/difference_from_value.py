
def difference_from_value(column, value):
    diff = [0] * len(column)
    for i in range(len(column)):
        diff[i] = column[i] - value
    
    return diff

def under_value(column, value):
    diff = [0] * len(column)
    for i in range(len(column)):
        if column[i] <= value:
            diff[i] = 1

    return diff

def over_value(column, value):
    diff = [0] * len(column)
    for i in range(len(column)):
        if column[i] >= value:
            diff[i] = 1

    return diff
