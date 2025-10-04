from queue import Queue

adj_list = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'I'],
    'F': ['J', 'H', 'C'],
    'G': ['C'],
    'H': ['F'],
    'I': ['E'],
    'J': ['F']
}

visited={}
parent={}
dfs_traversal=[]

for node in adj_list.keys():
    visited[node]=False
    parent[node]=None

def dfs(u):
    visited[u]=True
    dfs_traversal.append(u)

    for v in adj_list[u]:
        if not visited[v]:
            visited[v]=True
            parent[v]=u
            dfs(v)

source='A'
dfs(source)

node='H'
path=[]
while node is not None:
    path.append(node)
    node=parent[node]

path.reverse()
print("Shortest path is:",path)
print("DFS traversal:", dfs_traversal)
print("Parents:", parent)
