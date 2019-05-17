import sys
sys.setrecursionlimit(10**6)

graph = {i:[] for i in range(1, 100001)}
graph_reversed = {i:[] for i in range(1, 100001)}
cc_graph = {i:[] for i in range(1, 100001)}
edges = list()
visited = [False] * 100001
visited_reversed = [False] * 100001
visited_cc = [False] * 100001
stack = []
cc_stack = []
global cc_count
cc_count = 0
connected_components = [-1] * 100001

def get_neighbours(v):
    visited[v] = True

    for vertex in graph[v]:
        if visited[vertex] == False:
            get_neighbours(vertex)
    stack.append(v)

def get_reversed_neighbour(v):
    visited_reversed[v] = True
    connected_components[v] = cc_count
    for vertex in graph_reversed[v]:
        if visited_reversed[vertex] == False:
            get_reversed_neighbour(vertex)

def cc_neighbour(cc):
    visited_cc[cc] = True
    for elem in cc_graph[cc]:
        if visited_cc[elem] == False:
            cc_neighbour(elem)
    cc_stack.append(cc)
 
def dfs_traversal(v):
    for i in range(1, v+1):
        if visited[i] == False:
            get_neighbours(i)

def reversed_traversal():
    global cc_count
    for vertex in reversed(stack):
        if visited_reversed[vertex] == False:
            cc_count += 1
            get_reversed_neighbour(vertex)

def cc_traversal(cc_count):
    for i in range(1, cc_count + 1):
        if visited_cc[i] == False:
            cc_neighbour(i)

def max_cost():
    v, e = map(int, input().split(' '))
    
    for i in range(e):
        u, v = map(int, input().split(' '))
        graph[u].append(v)
        graph_reversed[v].append(u)
        edges.append((u,v))
    
    dfs_traversal(v)
    reversed_traversal()

    for i in range(e):
        if connected_components[edges[i][0]] != connected_components[edges[i][1]]:
            cc_graph[connected_components[edges[i][0]]].append(connected_components[edges[i][1]])

    cc_traversal(cc_count)

    dist = [0] * (cc_count + 1)

    while len(cc_stack) != 0:
        node = cc_stack.pop()
        for neighbour in cc_graph[node]:
            dist[neighbour] = max(dist[neighbour], 1 + dist[node])
    print(max(dist))

if __name__ == '__main__':
    max_cost()
