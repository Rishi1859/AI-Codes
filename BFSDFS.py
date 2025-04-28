from collections import deque

# Undirected Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Recursive DFS
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    print(node, end=' ')
    visited.add(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Run DFS
print("DFS Traversal:")
dfs_recursive(graph, 'A')

print("\n\nBFS Traversal:")
# Run BFS
bfs(graph, 'A')
