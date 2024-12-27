import re
from collections import defaultdict

def parse(lines):
    robot_re = re.compile(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)')
    points, velocities = [], []
    for line in lines:
        if not line:
            continue
        py, px, vy, vx = robot_re.findall(line)[0]
        points.append((int(px), int(py)))
        velocities.append((int(vx), int(vy)))
    return points, velocities

def one(points, velocities):
    n, m = 101, 103
    grid = [[0] * m for i in range(n)]
    secs = 100
    for p, v in zip(points, velocities):
        x = (p[0] + v[0] * secs + n * secs) % n
        y = (p[1] + v[1] * secs + m * secs) % m
        grid[x][y] += 1
    return (
        sum(sum(grid[i][j] for j in range(m // 2)) for i in range(n // 2)) *
        sum(sum(grid[i][j] for j in range(m // 2)) for i in range(n // 2 + 1, n)) *
        sum(sum(grid[i][j] for j in range(m // 2 + 1, m)) for i in range(n // 2)) *
        sum(sum(grid[i][j] for j in range(m // 2 + 1, m)) for i in range(n // 2 +1, n))
    )

def find_top(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 0:
                return (i, j)

def print_grid(grid):
    for i in range(len(grid)):
        s = ''
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                s += '.'
            else:
                s += str(grid[i][j])
        print(s)

def is_christmas_tree(top, grid):
    n, m = len(grid), len(grid[0])
    sx, sy = top
    grid[sx][sy] = 0
    width = 1
    while True:
        sx += 1
        if sy - width < 0 or sy + width == m or sx == n:
            break
        if grid[sx][sy - width] == 0 or grid[sx][sy + width] == 0:
            break
        width += 1
    if width > 10:
        print(width)
        return True
    return False


def is_christmas_tree_wrong(top, grid):
    n, m = len(grid), len(grid[0])
    sx, sy = top
    grid[sx][sy] = 0
    width = 1
    while True:
        sx += 1
        if sy - width < 0 or sy + width == m or sx == n:
            break
        if sum(grid[sx][sy-width:sy+width+1]) == 0:
            break
        for i in range(sy - width, sy + width + 1):
            if grid[sx][i] == 0:
                return False
            grid[sx][i] = 0
        width += 1
    if width > 1:
        print_grid(grid)
    return sum(sum(grid[i]) for i in range(n)) < 100

def has_christmas_tree(top, robots, n, m, cycles):
    sx, sy = top
    width = 1
    secs = defaultdict(list)
    for width in range(1, 50):
        sx += 1
        if sy - width < 0 or sy + width >= m or sx == n:
            break
        for i in range(sy - width, sy + width + 1):
            for j, s in cycles[sx][i]:
                secs[j].append(s)
        if len(secs.keys()) == robots:
            return True, secs
    return False, {}

def calc_cycle(i, p, v, n, m, grid):
    x = (p[0] + v[0]) % n
    y = (p[1] + v[1]) % m
    secs = 1
    start = 0
    pos = {}
    while x != p[0] or y != p[1]:
        x = (p[0] + v[0] * secs) % n
        y = (p[1] + v[1] * secs) % m
        if (x, y) in pos:
            start = secs - pos[(x, y)]
            break
        pos[(x, y)] = secs
        # grid[x][y].append((i, secs))
        secs += 1
    return secs, start

def calc_grid(points, velocities, n, m, secs):
    grid = [[0] * m for i in range(n)]
    for p, v in zip(points, velocities):
        x = (p[0] + v[0] * secs) % n
        y = (p[1] + v[1] * secs) % m
        grid[x][y] += 1
    return grid

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(secs):
    ans = secs[0]
    common_gcd = secs[0]
    for sec in secs:
        common_gcd = gcd(common_gcd, sec)
        ans *= sec
        ans //= common_gcd
    return ans

def two(points, velocities):
    n, m = 103, 101
    cycles = [[[] for i in range(m)] for j in range(n)]
    all_cycles = []
    for i in range(len(points)):
        length, start = calc_cycle(i, points[i], velocities[i], n, m, cycles)
        all_cycles.append(length)

    ans = float('inf')
    for secs in range(lcm(all_cycles)):
        grid = calc_grid(points, velocities, n, m, secs)
        for i in range(n):
            for j in range(m):
                top = (i, j)
                if not grid[i][j]:
                    continue
                if is_christmas_tree(top, grid):
                    print_grid(grid)
                    ans = min(ans, secs)
    return ans

fin = open('d14_in.txt', 'r')
fout = open('d14_out.txt', 'w')

lines = fin.readlines()
points, velocities = parse(lines)

fout.write(str(two(points, velocities)))

fin.close()
fout.close()
