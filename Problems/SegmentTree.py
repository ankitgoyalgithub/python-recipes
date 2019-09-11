def build(tree, node, start, end):
    print(tree, node, start, end)
    if start == end:
        tree[node] = tree[start]
    else:
        mid = int((start+end)/2)
        left = 2*node + 1
        right = 2 * node + 2

        if left < len(tree):
            build(tree, 2*node + 1, start, mid) 
        
        if right < len(tree):
            build(tree, 2*node + 2, mid+1, end)
        
        if right < len(tree):
            tree[node] = tree[2*node + 1] + tree[2*node + 2] 

if __name__ == '__main__':
    tree = [1,3,5,7,9,11]
    build(tree, 0, 0, 5)
    print(tree)