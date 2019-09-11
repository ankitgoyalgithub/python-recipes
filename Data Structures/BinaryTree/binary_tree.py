class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.horizontal_distnce = 0

class BinaryTree:
    def __init__(self, root):
        self.root = root
    
    def top_view(self, root):
        if root == None:
            return

        queue = list()
        queue.append(root)
        root.horizontal_distnce = 0
        dist_map = dict()

        while len(queue):
            curr_node = queue[0]
            hd = curr_node.horizontal_distnce

            if hd not in dist_map:
                dist_map[hd] = curr_node.data
            
            if curr_node.left:
                curr_node.left.horizontal_distnce = hd - 1
                queue.append(curr_node.left)
            
            if curr_node.right:
                curr_node.right.horizontal_distnce = hd + 1
                queue.append(curr_node.right)
            
            queue.pop(0)
        
        for i in sorted(dist_map):
            print(dist_map[i],end=" ")
        print()

    def top_view_recursive(self, root, hd, dist_map=dict()):
        if root == None:
            return
        
        if hd not in dist_map:
            dist_map[root.horizontal_distnce] = root.data
        
        self.top_view_recursive(root.left, hd-1, dist_map)
        self.top_view_recursive(root.right, hd+1, dist_map)

    def top_view_recursive_start(self, root):
        if root == None:
            return
        dist_map = dict()

        root.horizontal_distnce = 0
        self.top_view_recursive(root, 0, dist_map)

        for i in sorted(dist_map):
            print(dist_map[i],end=" ")
        print()
    
    def left_view_recursive(self, root, curr_level, max_level):
        if root == None:
            return
        
        if curr_level > max_level[0]:
            print(root.data, end=" ")
            max_level[0] = curr_level
        
        if root.left:
            self.left_view_recursive(root.left, curr_level+1, max_level)

        if root.right:
            self.left_view_recursive(root.right, curr_level+1, max_level)

    def left_view(self, root):
        if root == None:
            return
        
        max_level = [0]
        self.left_view_recursive(root, 1, max_level)
        print()

    def right_view_recursive(self, root, curr_level, max_level):
        if root == None:
            return
        
        if curr_level > max_level[0]:
            print(root.data, end=" ")
            max_level[0] = curr_level
        
        if root.right:
            self.right_view_recursive(root.right, curr_level+1, max_level)

        if root.left:
            self.right_view_recursive(root.left, curr_level+1, max_level)

    def right_view(self, root):
        if root == None:
            return
        
        max_level = [0]
        self.right_view_recursive(root, 1, max_level)
        print()
    
    def bottom_view_recursive(self, root, hd, level, dist_map, level_map):
        if root == None:
            return 
        
        if hd in dist_map:
            if level_map[hd] < level:
                dist_map[hd] = [root.data]
                level_map[hd] = level
            elif level_map[hd] == level:
                dist_map[hd].append(root.data)
        else:
            dist_map[hd] = [root.data]
            level_map[hd] = level

        print(dist_map)

        if root.left:
            self.bottom_view_recursive(root.left, hd - 1, level + 1,  dist_map, level_map)
        
        if root.right:
            self.bottom_view_recursive(root.right, hd + 1, level + 1, dist_map, level_map)

    
    def bottom_view(self, root):
        if root == None:
            return 

        dist_map = dict()
        level_map = dict()
        self.bottom_view_recursive(root, 0, 1, dist_map, level_map)

        for i in sorted(dist_map):
            for x in dist_map[i]:
                print(x, end=" ")
        print()

    def max_depth(self, root):
        if root == None:
            return 0
        
        l_depth = self.max_depth(root.left) 
        r_depth = self.max_depth(root.right)

        if l_depth > r_depth:
            return l_depth + 1
        else:
            return r_depth + 1



if __name__ == '__main__':
    root = Node(1)
    tree = BinaryTree(root)

    child2 = Node(2)
    child3 = Node(3)
    child4 = Node(4)
    child5 = Node(5)
    child6 = Node(6)
    child7 = Node(7)

    root.left = child2
    root.right = child3
    child2.left = child4
    child2.right = child5
    child3.left = child6
    child3.right = child7

    tree.top_view(root)
    tree.top_view_recursive_start(root)
    tree.left_view(root)
    tree.right_view(root)
    tree.bottom_view(root)

    print(tree.max_depth(root))


    
        