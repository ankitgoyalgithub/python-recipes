class Queue(object):

    def __init__(self, max_size=10):
        self.max_size = max_size
        self.front = 0
        self.rear = 0
        self.data = [0 for i in range(max_size)]
    
    def enqueue(self, data=None):
        if self.rear == self.max_size:
            raise Exception("Queue Full")
        
        self.data[self.rear] = data
        self.rear += 1

    def dequeue(self):
        if self.front == self.rear:
            raise Exception("Queue Empty")

        value = self.data[self.front]
        self.front += 1
        return value

if __name__ == '__main__':
    q = Queue(10)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(8)
    q.enqueue(9)
    q.enqueue(10)