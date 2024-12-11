from collections import deque
def parse(lines):
    n, m = len(lines), len(lines[0].strip())
    grid = [[None] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            grid[i][j] = int(lines[i][j])
    return grid

def bfs(p, grid, all_paths=False):
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
    queue = deque()
    queue.append(p)
    visited = [[0] * len(grid[0]) for i in range(len(grid))]
    visited[p[0]][p[1]] = 1
    ans = 0
    while len(queue) > 0:
        p = queue.popleft()
        value = grid[p[0]][p[1]]
        if value == 9:
            ans += visited[p[0]][p[1]]
            continue
        for dx, dy in directions:
            new_x, new_y = p[0] + dx, p[1] + dy
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                if visited[new_x][new_y]:
                    if all_paths:
                        visited[new_x][new_y] += visited[p[0]][p[1]]
                    continue
                if grid[new_x][new_y] == value + 1:
                    queue.append((new_x, new_y))
                    visited[new_x][new_y] += visited[p[0]][p[1]]
    return ans


def one(grid):
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0:
                continue
            ans += bfs((i, j), grid)
            print(i, j, ans)
    return ans

def two(grid):
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0:
                continue
            ans += bfs((i, j), grid, all_paths=True)
    return ans

fin = open('d10_in.txt', 'r')
fout = open('d10_out.txt', 'w')

lines = fin.readlines()
grid = parse(lines)

fout.write(str(two(grid)))

fin.close()
fout.close()
