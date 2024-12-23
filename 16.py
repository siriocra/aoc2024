import heapq
from collections import deque

def parse(lines):
    grid = []
    for line in lines:
        if line:
            grid.append(line.strip())
    return grid

def find_symbol(grid, symbol):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == symbol:
                return (i, j)

directions = ((0, 1), (-1, 0), (0, -1), (1, 0))

def cost(direction, facing):
    dist = abs(direction - facing)
    if dist == 3:
        dist = 1
    return dist * 1000 + 1

def calculate_distances(grid, start):
    distances = [[[float('infinity') for k in range(len(directions))] for j in range(len(grid[0]))] for i in range(len(grid))]
    prev = [[[[] for k in range(len(directions))] for j in range(len(grid[0]))] for i in range(len(grid))]
    distances[start[0]][start[1]][0] = 0

    pq = [(0, start, 0)]
    while len(pq) > 0:
        cur_d, cur_p, facing = heapq.heappop(pq)
        if cur_d > distances[cur_p[0]][cur_p[1]][facing]:
            continue
        for direction in range(len(directions)):
            neighbor = (cur_p[0] + directions[direction][0], cur_p[1] + directions[direction][1])
            if grid[neighbor[0]][neighbor[1]] == '#':
                continue
            distance = cur_d + cost(direction, facing)

            if distance < distances[neighbor[0]][neighbor[1]][direction]:
                distances[neighbor[0]][neighbor[1]][direction] = distance
                heapq.heappush(pq, (distance, neighbor, direction))
                prev[neighbor[0]][neighbor[1]][direction] = [(cur_p, facing)]
            elif distance == distances[neighbor[0]][neighbor[1]][direction]:
                prev[neighbor[0]][neighbor[1]][direction].append((cur_p, facing))

    return distances, prev

def one(grid):
    start, end = find_symbol(grid, 'S'), find_symbol(grid,'E')
    distances, _ = calculate_distances(grid, start)
    return min(distances[end[0]][end[1]])

def two(grid):
    start, end = find_symbol(grid, 'S'), find_symbol(grid,'E')
    distances, prev = calculate_distances(grid, start)
    visited = [[[False] * len(directions) for j in range(len(grid[0]))] for i in range(len(grid))]
    q = deque()
    mind = min(distances[end[0]][end[1]])
    for d in range(len(directions)):
        if distances[end[0]][end[1]][d] == mind:
            q.append((end, d))
            visited[end[0]][end[1]][d] = True
    while q:
        p, d = q.popleft()
        for neighbor, direction in prev[p[0]][p[1]][d]:
            if not visited[neighbor[0]][neighbor[1]][direction]:
                visited[neighbor[0]][neighbor[1]][direction] = True
                q.append((neighbor, direction))
    ans = 0
    for l in visited:
        for v in l:
            if v.count(True) > 0:
                ans += 1
    return ans

fin = open('d16_in.txt', 'r')
fout = open('d16_out.txt', 'w')

lines = fin.readlines()
grid = parse(lines)

fout.write(str(two(grid)))

fin.close()
fout.close()
