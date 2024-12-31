from collections import deque

def parse(lines):
    drops = []
    for line in lines:
        if line:
            y, x = list(map(int, line.strip().split(',')))
            drops.append((x, y))
    return drops

def corrupt(grid, drops, m):
    for i in range(m):
        grid[drops[i][0]][drops[i][1]] = '#'

directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

def is_reachable(drops, n, m):
    grid = [[0] * n for i in range(n)]
    visited = [[False] * n for i in range(n)]
    corrupt(grid, drops, m)

    start = (0, 0)
    visited[0][0] = True
    queue = deque()
    queue.append(start)
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            if not(0 <= x+dx < n and 0 <= y+dy < n):
                continue
            if grid[x+dx][y+dy] == '#':
                continue
            if visited[x+dx][y+dy]:
                continue
            visited[x+dx][y+dy] = True
            grid[x+dx][y+dy] = grid[x][y] + 1
            queue.append((x+dx, y+dy))
    return grid[n-1][n-1]

def one(drops):
    # n, m = 7, 12
    n, m = 71, 1024
    return is_reachable(drops, n, m)

def two(drops):
    # n = 7
    n = 71
    l = 0
    r = len(drops)
    while l + 1 < r:
        m = (r + l) // 2
        if is_reachable(drops, n, m):
            l = m
        else:
            r = m
    return str(drops[l][1]) + ',' + str(drops[l][0])

fin = open('d18_in.txt', 'r')
fout = open('d18_out.txt', 'w')

lines = fin.readlines()
drops = parse(lines)

fout.write(str(two(drops)))

fin.close()
fout.close()
