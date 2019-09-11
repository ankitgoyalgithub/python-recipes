class Heap:
    def __init__(self, size):
        self.data = []
        self.size = size
    
    def insert(self, value):
        if len(self.data) == self.size:
            raise Exception("Heap Full")
        else:
            self.data.append(value)
    
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

        if (l < n) and (self.data[l] > self.data[i]):
            largest = l
        
        if (r < n) and (self.data[r] > self.data[largest]):
            largest = r
        
        if largest != i:
            self.data[largest], self.data[i] = self.data[i], self.data[largest]
            self.heapify(n, largest)

    def build_heap(self):
        for i in range(int(self.size/2), -1, -1):
            self.heapify(len(self.data), i)
    
    def sort(self):
        n = self.size
        for i in range(n-1, 0, -1): 
            self.data[i], self.data[0] = self.data[0], self.data[i]
            self.heapify(i, 0) 

if __name__ == '__main__':
    h = Heap(size=9)

    a = [4,2,1,3,5,6,7,8,9]

    for i in a:
        h.insert(i)
    h.build_heap()
    h.sort()

    print(h.data)
