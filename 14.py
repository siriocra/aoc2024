import re

def parse(lines):
    robot_re = re.compile(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)')
    points, velocities = [], []
    for line in lines:
        if not line:
            continue
        px, py, vx, vy = robot_re.findall(line)[0]
        points.append((int(px), int(py)))
        velocities.append((int(vx), int(vy)))
    return points, velocities

def one(points, velocities):
    n, m = 11, 7
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


def two():
    pass

fin = open('d14_in.txt', 'r')
fout = open('d14_out.txt', 'w')

lines = fin.readlines()
points, velocities = parse(lines)

fout.write(str(one(points, velocities)))

fin.close()
fout.close()
