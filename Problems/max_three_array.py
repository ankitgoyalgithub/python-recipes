import sys
import math

def max_three(l=None):
    top_3 = []

    for i in l:
        if len(top_3) < 3:
            top_3.append(i)
        else:
            min_top_3 = min(top_3)
            if i > min_top_3:
                del top_3[top_3.index(min_top_3)]
                top_3.append(i)
    return sum(top_3)



if __name__ == '__main__':
    l = [5,9,1,4,3,0,2,7,8]

    print(max_three(l))