graph = {
    0: [1 , 2],
    1: [0 , 3 , 4],
    2: [0 , 5 , 6],
    3: [1],
    4: [1, 6],
    5: [2],
    6: [2, 4]
}

def graphColoring(graph):
    nodeColors = {}
    bestSolution = float('inf')
    def isValid(node, color):
        for adjNode in graph[node]:
            if nodeColors.get(adjNode) == color:
                return False
        return True

    def backtrack(nonColoredNodes):
        nonlocal bestSolution
        if not nonColoredNodes:
            max_colors = max(nodeColors.values())
            bestSolution = min(max_colors+1, bestSolution)
            return
        node = nonColoredNodes.pop()
        for color in range(min(len(graph), bestSolution)):
            if isValid(node, color):
                nodeColors[node] = color
                backtrack(nonColoredNodes.copy())
                del nodeColors[node]
        nonColoredNodes.append(node)

    nonColoredNodes = list(graph.keys())
    backtrack(nonColoredNodes)
    return bestSolution

print(f"Minimum no. of Colors Reuqired to Color the Graph: {graphColoring(graph)}")