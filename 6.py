direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def parse(lines):
    return [list(s.strip()) for s in lines]

def find_guard(lab, n, m):
    for i in range(n):
        for j in range(m):
            if lab[i][j] == '^':
                return (i, j)

def has_loop(lab, guard_x, guard_y):
    n, m = len(lab), len(lab[0])
    visited = [[[False] * len(direction) for i in range(n)] for j in range(m)]
    cur_dir = 0
    while (0 <= guard_x + direction[cur_dir][0] < n and
                    0 <= guard_y + direction[cur_dir][1] < m):
        new_x = guard_x + direction[cur_dir][0]
        new_y = guard_y + direction[cur_dir][1]
        while lab[new_x][new_y] == '#':
            cur_dir = (cur_dir + 1) % len(direction)
            new_x = guard_x + direction[cur_dir][0]
            new_y = guard_y + direction[cur_dir][1]
        if visited[new_x][new_y][cur_dir]:
            return True, None
        visited[new_x][new_y][cur_dir] = True
        guard_x = new_x
        guard_y = new_y
    return False, visited

def one(lab):
    guard_x, guard_y = find_guard(lab, len(lab), len(lab[0]))
    _, visited = has_loop(lab, guard_x, guard_y)
    return sum(visited[i][j].count(True) > 0 for i in range(len(visited)) for j in range(len(visited[0]))) 


def two(lab):
    guard_x, guard_y = find_guard(lab, len(lab), len(lab[0]))
    _, visited = has_loop(lab, guard_x, guard_y)
    ans = 0
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if lab[i][j] == '.' and visited[i][j].count(True) > 0:
                lab[i][j] = '#'
                loop, _ = has_loop(lab, guard_x, guard_y)
                if loop:
                    ans += 1
                lab[i][j] = '.'
    return ans

fin = open('d6_in.txt', 'r')
fout = open('d6_out.txt', 'w')

lines = fin.readlines()
lab = parse(lines)

fout.write(str(two(lab)))

fin.close()
fout.close()
