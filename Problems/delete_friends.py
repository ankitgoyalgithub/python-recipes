class Node:
    def __init__(self,data):
        self.data = data
        self.nxt = None
    
class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
    
    def insert(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.nxt = node
            self.tail = node
    
    def display(self):
        if not self.head:
            return
        else:
            temp = self.head
            while temp:
                print(temp.data,end=" ")
                temp = temp.nxt
            print()
    
    def delete_friends(self, k):
        while k > 0:
            if (not self.head) or (self.head.nxt is None):
                self.head = None
                
            delete_friend = False
            temp = self.head
            prev_temp = None
            
            while (temp and temp.nxt):
                if temp.data < temp.nxt.data:
                    if temp == self.head:
                        self.head = temp.nxt
                        temp = self.head
                    else: 
                        prev_temp.nxt = temp.nxt
                        temp = prev_temp.nxt
                    delete_friend = True
                    break
                prev_temp = temp
                temp = temp.nxt
            
            if not delete_friend:
                temp = self.head
                
                if (not temp) or (temp.nxt is None):
                    self.head = None
                else:
                    while temp.nxt.nxt:
                        temp = temp.nxt
                    
                    temp.nxt = None
            
            k -= 1
                
t = int(input())

while t>0:
    n,k = map(int, input().split(" "))
    friends = map(int, input().split(" "))
    friend_list = LinkedList()
    
    for people in friends:
        friend = Node(people)
        friend_list.insert(friend)
    
    friend_list.delete_friends(k)
    friend_list.display()
    
    t -= 1