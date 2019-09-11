def overlap(i1 = None, i2 = None):
    if ((i1[0] > i2[0]) and (i1[0] < i2[1])) or ((i2[0] > i1[0]) and (i2[0] < i1[1])):
        return True
    
    return False

def merge(i1=None, i2=None):
    if (i1[0] > i2[0]) and (i1[0] < i2[1]):
        if i1[1] > i2[1]:
            return [i2[0], i1[1]]
        else:
            return [i2[0], i2[1]]
    elif (i2[0] > i1[0]) and (i2[0] < i1[1]):
        if i2[1] > i1[1]:
            return [i1[0], i2[1]]
        else:
            return [i1[0], i1[1]]

def merge_intervals(intervals = None):
    if len(intervals) == 1:
        return intervals
    else:
        temp = intervals

        temp = sorted(temp, key = lambda x: x[0])
        interval_stack = [temp[0]]

        for index in range(1, len(temp)):
            top = interval_stack[-1]
            
            if overlap(temp[index], top):
                interval_stack[-1] = merge(temp[index], top)
            else:
                interval_stack.append(temp[index])
    
    return interval_stack


if __name__ == '__main__':
    intervals = [[6,8], [1,3], [2,4], [5,7]]
    print(merge_intervals(intervals))