class BinaryTree:
    
    def __init__(self, left, right):
        self.left = left
        self.right = right

if __name__ == '__main__':
    t = BinaryTree(BinaryTree('A', 'B'), BinaryTree('C', 'D'))
    print(t.right.left)