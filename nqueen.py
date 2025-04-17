def nqueen(n):
    cols = set()
    posDig = set()
    negDig = set()

    res = []
    board = [["."] * n for _ in range(n)]

    def backtrack(r):
        if r == n:
            copy_board = ["".join(row) for row in board]
            res.append(copy_board)
            return
            
        for c in range(n):
            if c in cols or (r-c) in posDig or (r+c) in negDig:
                continue

            cols.add(c)
            posDig.add(r-c)
            negDig.add(r+c)
            board[r][c] = 'Q'

            backtrack(r+1)

            cols.remove(c)
            posDig.remove(r-c)
            negDig.remove(r+c)
            board[r][c] = '.'
    
    backtrack(0)
    return res            

print(nqueen(4))
print()

for i, s in enumerate(nqueen(4)):
    print(f"Solution {i+1}:")
    for r in s:
        print("  ".join(r))
    print()