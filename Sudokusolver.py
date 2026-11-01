def is_valid(b,r,c,n):
    for i in range(9):
        if b[r][i] == n or b[i][c] == n:
            return False

    br,bc = 3*(r//3), 3*(c//3)
    for r in range(br, br+3):
        for c in range(bc, bc+3):
            if b[r][c] == n:
                return False
    return True

def options(b,r,c):
    return[n for n in range(1,10) if is_valid(b,r,c,n)]

def solve(b):
    best, opts = None, None

    for r in range(9):
        for c in range(9):
            if b[r][c] == 0:
                o = options(b,r,c)
                if not o:
                    return False
                if opts is None or len(o) < len(opts):
                    best, opts = (r,c) , o

    if best is None:
        return True
    r, c = best 
    for n in opts:
        b[r][c] = n
        if solve(b):
            return True
        b[r][c] = 0
    return False

board = [[5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]]

if solve(board):
    for row in board:
        print(*row)
else:
    print("NO solution found")
