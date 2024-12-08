from collections import defaultdict

def parse(lines):
    grid = defaultdict(list)
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        for j in range(len(lines[0])):
            if lines[i][j] != '.':
                grid[lines[i][j]].append((i,j))
    return grid, (len(lines), len(lines[0]))

def calculate_antidotes(p1, p2, findall=False):
    res = []
    if findall:
        res.append(p1)
        res.append(p2)
    d = (p2[0] - p1[0], p2[1] - p1[1])
    n1 = (p1[0] - d[0], p1[1] - d[1])
    while 0 <= n1[0] < size[0] and 0 <= n1[1] < size[1]:
        res.append(n1)
        if not findall:
            break
        n1 = (n1[0] - d[0], n1[1] - d[1])

    n2 = (p2[0] + d[0], p2[1] + d[1])
    while 0 <= n2[0] < size[0] and 0 <= n2[1] < size[1]:
        res.append(n2)
        if not findall:
            break
        n2 = (n2[0] + d[0], n2[1] + d[1])

    return res

def one(grid, size):
    antidotes = [[False] * size[1] for i in range(size[0])]
    for _, points in grid.items():
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                a = calculate_antidotes(points[i], points[j])
                for x, y in a:
                    antidotes[x][y] = True
    return sum(antidotes[i].count(True) for i in range(len(antidotes)))
                

def two(grid, size):
    antidotes = [[False] * size[1] for i in range(size[0])]
    for _, points in grid.items():
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                a = calculate_antidotes(points[i], points[j], findall=True)
                for x, y in a:
                    antidotes[x][y] = True
    return sum(antidotes[i].count(True) for i in range(len(antidotes)))


fin = open('d8_in.txt', 'r')
fout = open('d8_out.txt', 'w')

lines = fin.readlines()
grid, size = parse(lines)

fout.write(str(two(grid, size)))

fin.close()
fout.close()
