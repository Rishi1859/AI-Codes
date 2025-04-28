from heapq import heappop, heappush

def EightPuzzleHeuristic(board):
    target = "123456780"
    adj = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4, 6],
        4: [1, 3, 5, 7],
        5: [2, 4, 8],
        6: [3, 7],
        7: [4, 6, 8],
        8: [5, 7]
    }
    def heuristic(state):
        return sum(1 for i in range(9) if state[i]!='0' and state[i]!=target[i])

    b = ''.join(str(c) for row in board for c in row)
    heap = [(heuristic(b), 0, b, b.index('0'))]
    visited = set()
    while heap:
        f, g, b, i = heappop(heap)
        if b == target:
            return g
        b_arr = list(b)
        for j in adj[i]:
            new_b_arr = b_arr.copy()
            new_b_arr[i], new_b_arr[j] = b_arr[j], b_arr[i]
            new_b = ''.join(new_b_arr)
            if new_b not in visited:
                visited.add(new_b)
                heappush(heap, (g+1+heuristic(new_b), g+1, new_b, j))
    return -1

print(EightPuzzleHeuristic(board=[[1,2,3], [4,5,6], [0,7,8]]))