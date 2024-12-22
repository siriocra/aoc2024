double_grid = {'.': ['.', '.'], 'O': ['[',']'], '@': ['@', '.'], '#': ['#', '#']}

def parse(lines, double=False):
    grid = []
    instructions = []
    for line in lines:
        if not line:
            continue
        if '#' in line:
            grid_l = []
            if double:
                for c in line.strip():
                    grid_l.extend(double_grid[c])
            else:
                grid_l = [c for c in line.strip()]
            grid.append(grid_l)
        else:
            instructions.append(line.strip())
    return grid, instructions

direction = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}

def get_robot(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                grid[i][j] = '.'
                return (i, j)

def move(robot, grid, direction):
    i, j = robot
    dx, dy = direction
    new_x, new_y = i + dx, j + dy
    while grid[new_x][new_y] == 'O':
        new_x += dx
        new_y += dy
    if grid[new_x][new_y] == '#':
        return robot
    else:
        grid[new_x][new_y] = 'O'
        grid[i+dx][j+dy] = '.'
        return (i + dx, j + dy)

def move_two(robot, grid, direction, check=False):
    i, j = robot
    dx, dy = direction
    new_x, new_y = i + dx, j + dy
    if abs(dy) > 0:
        while grid[new_x][new_y] == '[' or grid[new_x][new_y] == ']':
            new_x += dx
            new_y += dy
        if grid[new_x][new_y] == '#':
            return robot
        else:
            for y in range(min(new_y, j), max(new_y, j)):
                grid[i][y] = grid[i][y-dy]
            grid[i+dx][j+dy] = '.'
            return (i + dx, j + dy)
    else:
        if grid[new_x][new_y] == '[':
            r1 = move_two((i + dx, j + dy), grid, direction, True)
            r2 = move_two((i + dx, j + dy + 1), grid, direction, True)
            if r1 == robot or r2 == robot:
                return robot
            # TBD
        elif grid[new_x][new_y] == ']':
            # TBD
            pass
    

def checksum(grid):
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'O' or grid[i][j] == '[':
                ans += i * 100 + j
    return ans

def one(grid, instructions):
    robot = get_robot(grid)
    for l in instructions:
        for c in l:
             dx, dy = direction[c]
             robot = move(robot, grid, direction[c])
    return checksum(grid)

def two(grid, instructions):
    robot = get_robot(grid)
    for l in instructions:
        for c in l:
             dx, dy = direction[c]
             robot = move(robot, grid, direction[c])
    return checksum(grid)

fin = open('d15_in.txt', 'r')
fout = open('d15_out.txt', 'w')

lines = fin.readlines()
grid, instructions = parse(lines)

fout.write(str(one(grid, instructions)))

fin.close()
fout.close()
