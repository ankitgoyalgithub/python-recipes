class Heap:
    def __init__(self, size):
        self.length = 0
        self.size = size
        self.container = []
    
    def heapify(self, i):
        if 2*i + 1 < self.length:
            if self.container[2*i+1] > self.container[i]:
                largest = 2*i+1
            else:
                largest = i
            
            if 2*i + 2 < self.length:
                if  self.container[2*i+2] > self.container[largest]:
                    largest = 2*i+2
            
            if largest != i:
                self.container[i], self.container[largest] = self.container[largest], self.container[i]
                self.heapify(largest)
    
    def build_heap(self):
        start_index = int(self.length/2) - 1

        for i in range(start_index, -1, -1):
            self.heapify(i)

    def add(self, x):
        if self.length == self.size:
            raise Exception("Queue Full")
        else:
            self.length += 1
            self.container.append(x)
            self.heapify(0)

if __name__ == '__main__':
    h = Heap(10)
    h.add(1)
    h.add(2)
    h.add(5)
    h.add(4)
    h.add(3)
    print(h.container)
    
