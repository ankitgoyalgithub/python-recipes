from heapq import heappush as push, heappushpop as pushpop

class Spliter:
    def __init__(self):
        self.upper = []
        self.lower = []
        
    def median(self):
        if len(self.upper) > len(self.lower):
            return self.upper[0]
        else:
            return (self.upper[0] - self.lower[0]) / 2.
        
    def add(self, value):
        value = pushpop(self.upper, value)
        value = -pushpop(self.lower, -value)
        
        if len(self.upper) <= len(self.lower):
            push(self.upper, value)
        else:
            push(self.lower, -value)
        print('*****')
        print(value, len(self.upper), self.upper)
        print(value, len(self.lower), self.lower)
        print('*****')

if __name__ == '__main__':
    a = [1,2,3,4,5,6]

    sp = Spliter()

    for i in a:
        sp.add(i)
    print(sp.median())