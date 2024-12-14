from collections import deque

def parse(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    if not lines[-1]:
        lines = lines[:-1]
    return lines

directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

def count_neighbours(i, j, grid, visited):
    c = grid[i][j]
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    neighbours = 0
    area = 0
    while queue:
        p = queue.popleft()
        area += 1
        for dx, dy in directions:
            new_x, new_y = p[0] + dx, p[1] + dy
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                if grid[new_x][new_y] == c:
                    neighbours += 1
                    if not visited[new_x][new_y]:
                        queue.append((new_x, new_y))
                        visited[new_x][new_y] = True
    return area, neighbours


def one(grid):
    n, m = len(grid), len(grid[0])
    visited = [[False] * m for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                area, neighbours = count_neighbours(i, j, grid, visited)
                ans += area * (area * 4 - neighbours)
    return ans

def two():
    pass

fin = open('d12_in.txt', 'r')
fout = open('d12_out.txt', 'w')

lines = fin.readlines()
grid = parse(lines)

fout.write(str(one(grid)))

fin.close()
fout.close()
