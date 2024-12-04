def search_word(word, grid, i, j, n, m):
    ans = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            found = True
            for l in range(len(word)):
                nx = dx * l
                ny = dy * l
                if 0 <= nx + i < n and 0 <= ny + j < m:
                    if grid[nx+i][ny+j] != word[l]:
                        found = False
                        break
                else:
                    found = False
                    break
            if found:
                ans += 1
    return ans


def one(grid):
    n, m = len(grid), len(grid[0])
    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'X':
                ans += search_word('XMAS', grid, i, j, n, m)
    return ans


def check(pattern, grid, i, j):
    if len(pattern) + i > len(grid) or len(pattern[0]) + j > len(grid[0]):
        return False
    found = True
    for dx in range(len(pattern)):
        for dy in range(len(pattern[0])):
            if pattern[dx][dy] == '#':
                continue
            if grid[i+dx][j+dy] != pattern[dx][dy]:
                found = False
    return found

mas_patterns = [['M#S', '#A#', 'M#S'], ['M#M', '#A#', 'S#S'],
            ['S#M', '#A#', 'S#M'], ['S#S', '#A#', 'M#M']]

def find_patterns(patterns, grid):
    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for pattern in patterns:
                if check(pattern, grid, i, j):
                    ans += 1
    return ans

def two(grid):
    return  find_patterns(mas_patterns, grid)


fin = open('d4_in.txt', 'r')
fout = open('d4_out.txt', 'w')

lines = fin.readlines()

fout.write(str(two(lines)))

fin.close()
fout.close()
