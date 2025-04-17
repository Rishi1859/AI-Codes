from collections import deque

graph = {
    0: [1 , 2],
    1: [0 , 3 , 4],
    2: [0 , 5 , 6],
    3: [1],
    4: [1],
    5: [2],
    6: [2]
}

visited = set()
queue = deque([0])
def bfs(target):
    if not queue:
        return None
    node = queue.popleft()
    if node == target:
        return node
    visited.add(node)
    for adjNodes in graph[node]:
        if adjNodes not in visited:
            visited.add(adjNodes)
            queue.append(adjNodes)
    return bfs(target)

print(bfs(6))