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

def bfs(source, target, graph):
    queue = deque([source])
    visited = set([source])
    parent = {source:None}

    def bfs_helper():
        if not queue:
            return f'Node {target} Not Found'
        node = queue.popleft()
        if node == target:
            temp = node
            path = []
            while temp!=None:
                path.append(temp)
                temp = parent[temp]
            path.reverse()
            depth = len(path) - 1
            return f"Node {target} Found", path, depth
        for adjNode in graph[node]:
            if adjNode not in visited:
                parent[adjNode] = node
                queue.append(adjNode)
                visited.add(adjNode)
        return bfs_helper()

    return bfs_helper()

print(bfs(0, 3, graph))