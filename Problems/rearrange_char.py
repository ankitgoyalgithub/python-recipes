from collections import defaultdict

class Heap:
    def __init__(self):
        self.data = []
        self.size = 0

    def insert(self, value):
        self.data.append(value)
        self.size += 1

    @staticmethod
    def left(i):
        return 2*i + 1
    
    @staticmethod
    def right(i):
        return 2*i + 2

    def heapify(self, n, i):
        largest = i

        l = Heap.left(i)
        r = Heap.right(i)

        if (l < n) and (self.data[l][1] > self.data[i][1]):
            largest = l
        
        if (r < n) and (self.data[r][1] > self.data[largest][1]):
            largest = r
        
        if largest != i:
            self.data[largest], self.data[i] = self.data[i], self.data[largest]
            self.heapify(n, largest)

    def build_heap(self):
        for i in range(int(len(self.data)/2), -1, -1):
            self.heapify(len(self.data), i)
    
    def sort(self):
        n = self.size
        for i in range(n-1, 0, -1): 
            self.data[i], self.data[0] = self.data[0], self.data[i]
            self.heapify(i, 0) 

def solution(input_str):
    freq = defaultdict(int)
    hp = Heap()

    for c in input_str:
        freq[c] += 1
    
    for key in freq:
        hp.insert((key, freq[key]))
    
    previous = None
    hp.build_heap()

    result = []

    while len(hp.data) > 0:
        result.append(hp.data[0][0])
        temp = (hp.data[0][0], hp.data[0][1] - 1)
        del hp.data[0]

        if previous and previous[1] > 0:
            hp.insert(previous)
        
        previous = temp
        hp.build_heap()
    
    return ''.join(result)
        
if __name__ == "__main__":
    s = "baaabc"
    result = solution(s)

    if result == -1:
        print("Not Possible")
    else:
        print(result)