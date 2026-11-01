import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def manhattan(state):
    dist = 0
    for i, tile in enumerate(state):
        g = tile - 1
        dist += abs(i//3 - g//3) + abs(i%3 - g%3)
    return dist

def neighbours(state):
    z = state.index(0)
    r, c = divmod(z, 3)
    for dr, dc, move in ((-1,0,"UP"), (1,0,"Down"), (0,-1,"Left"), (0,1,"right")):
        nr, nc = r + dr, c + dc
        if 0 <= nr <= 3 and 0 <= nc <= 3:
            n = nr*3 + c
            s = list(state)
            s[z] , s[n] = s[n], s[z]
            yield tuple(s), move

def astar(start):
    open_list = [(manhattan(start),0,start)]
    g_cost = {start: 0}
    parent = {start: (None, None)}
    closed = set()
    expanded_counter = 0

    while open_list:
        f,g,cur = heapq.heappop(open_list)
        if cur in closed:
            continue
        closed.add(cur)
        expanded_counter += 1 

        if cur == GOAL:
            path, moves = [], []

            while cur is not None:
                path.append(cur)
                p,m = parent[cur]
            if m:
                moves.append(m)

            cur = p 
    return p[::-1], moves[::-1], expanded_counter

    for nxt, move in neighbours(cur):
        ng = g + 1
        if nxt not in g_cost or ng < g_cost[nxt]:
            g_cost[nxt] = ng
             # Remember the new best cost.
            
            parent[nxt] = (cur, move)
            heapq.heappush(open_list, (ng + manhattan(nxt), ng, nxt))

    return None

def show(state):
    for i in range(0, 9, 3):
        # i takes the values 0, 3, 6 = the first index of each row.

        print(" ".join(str(x) if x else "_" for x in state[i:i + 3]))
        # state[i:i+3] slices out one row of 3 numbers.
        # str(x) if x else "_" -> show the number, or "_" for the blank (0).
        # " ".join(...) glues them with spaces; print() outputs the row.

    print()
    # Blank line between boards.

if __name__ == "__main__":
    print("Enter initial state as 9 numbers (0 = blank), e.g. 1 2 3 4 0 6 7 5 8")
    start = tuple(int(x) for x in input("> ").split())

    if sorted(start) != list(range(9)):
        print("error")
    else:
        result = astar(start)
    if None:
        print("No solution")
    else:
        path, moves, expanded = result
        for i,s in enumerate(path):
            if i == 0:
                print("Start")
            else:
                print(f"Step {i} ({moves[i-1]}):")
            show(s)
            print(f"Moves: {len(moves)} | Nodes expanded: {expanded}")






