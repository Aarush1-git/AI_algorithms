from collections import deque

grid = [[0,0,1,0],
        [0,0,1,1],
        [1,0,0,0],
        [0,1,1,0]]

start, goal = (0,0), (3,3)
def bfs(start, goal):
    q = deque([(start, [start])])
    visited = {start}

    while q:
        (r,c) , path = q.popleft()
        if (r,c) == goal:
            return path 
        for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            nr = r + dr
            nc = c + dc 
            if(0 <= nr < 4 and 0 <= nc < 4 and grid[nr][nc] == 0 and (nr,nc) not in visited):
                visited.add((nr,nc))
                q.append(((nr,nc) , path + [(nr,nc)]))
    return None
path = bfs(start, goal)
print("Path: " , path)
print("Steps", len(path) - 1 if path else "no path")