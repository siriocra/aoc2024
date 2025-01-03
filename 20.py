from collections import deque

def parse(lines):
    start, end = None, None
    grid = [[None] * len(lines[0].strip()) for i in range(len(lines))]
    for i in range(len(lines)):
        for j in range(len(lines[0].strip())):
            if lines[i][j] == 'S':
                start = (i, j)
                grid[i][j] = '.'
            elif lines[i][j] == 'E':
                end = (i, j)
                grid[i][j] = '.'
            else:
                grid[i][j] = lines[i][j]
    return grid, start, end

directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

def bfs(grid, start):
    distance = [[None] * len(grid[0]) for i in range(len(grid))]
    queue = deque()
    queue.append(start)
    distance[start[0]][start[1]] = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            if not(0 <= x+dx < len(grid) and 0 <= y+dy < len(grid[0])):
                continue
            if grid[x+dx][y+dy] == '.' and distance[x+dx][y+dy] is None:
                queue.append((x+dx, y+dy))
                distance[x+dx][y+dy] = distance[x][y] + 1
    return distance

def calc_dist(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def cheat(grid, time, start, end):
    if not(0 <= end[0] < len(grid) and 0 <= end[1] < len(grid[0])):
        return None
    if grid[start[0]][start[1]] == '#':
        return None
    if grid[end[0]][end[1]] == '#':
        return None
    if time[start[0]][start[1]] > time[end[0]][end[1]] - calc_dist(start, end):
        return None
    return time[end[0]][end[1]] - time[start[0]][start[1]] - calc_dist(start, end)


def one(grid, start, end):
    n, m = len(grid), len(grid[0])
    time = bfs(grid, start)
    ans = 0
    for i in range(n):
        for j in range(m):
            for k in range(i - 2, i + 3):
                for l in range(j - 2, j + 3):
                    if calc_dist((i, j), (k, l)) == 2:
                        cheat_time = cheat(grid, time, (i, j), (k, l))
                        if cheat_time:
                            if cheat_time >= 100:
                                ans += 1
    return ans

def two(grid, start, end):
    n, m = len(grid), len(grid[0])
    time = bfs(grid, start)
    ans = 0
    max_dist = 20
    for i in range(n):
        for j in range(m):
            for k in range(i - max_dist, i + max_dist + 1):
                for l in range(j - max_dist, j + max_dist + 1):
                    if calc_dist((i, j), (k, l)) <= 20:
                        cheat_time = cheat(grid, time, (i, j), (k, l))
                        if cheat_time:
                            if cheat_time >= 100:
                                ans += 1
    return ans

fin = open('d20_in.txt', 'r')
fout = open('d20_out.txt', 'w')

lines = fin.readlines()
grid, start, end = parse(lines)

fout.write(str(two(grid, start, end)))

fin.close()
fout.close()
