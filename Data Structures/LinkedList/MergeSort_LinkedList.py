class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    @staticmethod
    def divide(source, first, end):
        slow = source
        fast = slow.next

        while fast:
            fast = fast.next
            if fast:
                slow = slow.next
                fast = fast.next
        
        first[0] = source
        end[0] = slow.next
        slow.next = None
    
    @staticmethod
    def merge_val(first, end):
        result = None
        
        if first[0] is None: 
            return end[0]
        elif end[0] is None: 
            return first[0]
  
        if first[0].data <= end[0].data: 
            result = first[0] 
            result.next = LinkedList.merge_val([first[0].next], [end[0]]) 
        else: 
            result = end[0]
            result.next = LinkedList.merge_val([first[0]], [end[0].next]) 
        return result

    def mergesort(self, head):
        if (head is None) or (head.next is None):
            return
        
        first = [None]
        end = [None]

        LinkedList.divide(head, first, end)
        self.mergesort(first[0])
        self.mergesort(end[0])
        self.head = LinkedList.merge_val(first, end)

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
    

if __name__ == '__main__':
    l = LinkedList()
    l.insert(1)
    l.insert(2)
    l.insert(3)
    l.insert(4)
    l.insert(5)
    l.insert(6)
    l.insert(7)
    l.insert(8)
    l.insert(9)
    l.display()
    l.mergesort(l.head)
    l.display()