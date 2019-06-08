class A:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

class B(A):
    def __init__(self,name):
        super().__init__('A')
        self.name = name
    
    def display(self):
        print(self.name)

if __name__ == '__main__':
    b = B('C')
    b.display()