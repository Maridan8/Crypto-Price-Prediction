
def sum_in_period_positive(l, period):
    sums = [0] * len(l)
    for i in range(period+1, len(l)):
        sum = 0
        for j in range(i-period, i):
            if ((l[j] - l[j-1]) > 0) :
                sum += (l[j] - l[j-1]) 
        sums[i] = sum

    return sums

def sum_in_period_negative(l, period):
    sums = [0] * len(l)
    for i in range(period+1, len(l)):
        sum = 0
        for j in range(i-period, i):
            if ((l[j] - l[j-1]) < 0) :
                sum += abs(l[j] - l[j-1]) 
        sums[i] = sum

    return sums