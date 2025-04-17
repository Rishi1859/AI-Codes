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

def dfs(node, target):
    if node == target:
        return node

    visited.add(node)
    
    for adjNode in graph[node]:
        if adjNode not in visited:
            res = dfs(adjNode, target)
            visited.add(adjNode)
            if res is not None:
                return res
    
    return None

print(dfs(0, 6))
