graph = {
    0: [1 , 2],
    1: [0 , 3 , 4],
    2: [0 , 5 , 6],
    3: [1],
    4: [1],
    5: [2],
    6: [2]
}

def dfs(source, target, graph):
    visited = set([source])
    parent = {source:None}

    def dfs_helper(node):
        if node == target:
            temp = node
            path = []
            while temp!=None:
                path.append(temp)
                temp = parent[temp]
            path.reverse()
            depth = len(path) - 1
            return f"Node {target} found", path, depth

        for adjNode in graph[node]:
            if adjNode not in visited:
                parent[adjNode] = node
                visited.add(adjNode)
                res = dfs_helper(adjNode)
                if res is not None:
                    return res
        return None
    
    return dfs_helper(source)

res = dfs(0, 6, graph)
if res:
    print(res)
else:
    print('Node not Found')