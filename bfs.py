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

visited = {}
level = {}
parent = {}
queue = Queue()
bfs_traversal = []

for node in adj_list.keys():
    visited[node] = False
    level[node] = -1
    parent[node] = None

source = 'A'
visited[source] = True
level[source] = 0
queue.put(source)

while not queue.empty():
    u = queue.get()
    bfs_traversal.append(u)

    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u] + 1
            queue.put(v)

node='H'
path=[]
while node is not None:
    path.append(node)
    node=parent[node]

path.reverse()
print("Shortest path is:",path)


print("BFS traversal:", bfs_traversal)
print("Levels:", level)
print("Parents:", parent)



"""from queue import Queue
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
queue=Queue()
level={}
parent={}
bfs_traversal=[]

for node in adj_list.keys():
    visited[node]=False
    parent[node]=None
    level[node]=-1

source='A'
visited[source]=True
level[source]=0
queue.put(source)

while not queue.empty():
    u=queue.get()
    bfs_traversal.append(u)

    for v in adj_list[u]:
      if not visited [v]:
        visited[v]=True
        parent[v]=u
        level[v]=level[u]+1
        queue.put(v)

node='H'
path=[]
while node is not None:
    path.append(node)
    node=parent[node]

path.reverse()

print("Shortest path is:",path)


print("BFS traversal:", bfs_traversal)
print("Levels:", level)
print("Parents:", parent)
    
    """




































