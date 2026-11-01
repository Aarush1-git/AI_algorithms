CA,CB,GOAL = 4,3,2

def moves(a,b):
    return[
        (CA,b),
        (a,CB),
        (0,b),
        (a,0),
        (a - min(a, CB-b), b + min(a, CB-b)),
        (a + min(b, CA-a), b - min(b, CA-a))
    ]

def dfs(state,visited,path):
    visited.add(state)
    path.append(state)
    if state[0] == GOAL:
        return True
    for move in moves(*state):
        if move not in visited and dfs(move,visited,path):
            return True
    path.pop()
    return False

path = []
if dfs((0,0),set(), path):
    for s in path:
        print(s)
else:
    print("No solution")