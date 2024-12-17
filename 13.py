import re

A_RE = re.compile(r'Button A: X\+(\d+), Y\+(\d+)')
B_RE = re.compile(r'Button B: X\+(\d+), Y\+(\d+)')
PRIZE_RE = re.compile(r'Prize: X=(\d+), Y=(\d+)')

def parse(lines):
    buttons_a, buttons_b = [], []
    prizes = []
    for line in lines:
        if A_RE.match(line):
            res = A_RE.findall(line)
            buttons_a.append((int(res[0][0]), int(res[0][1])))
        elif B_RE.match(line):
            res = B_RE.findall(line)
            buttons_b.append((int(res[0][0]), int(res[0][1])))
        elif PRIZE_RE.match(line):
            res = PRIZE_RE.findall(line)
            prizes.append((int(res[0][0]), int(res[0][1])))
    return buttons_a, buttons_b, prizes

def is_answer(a, count_a, b, count_b, prize):
    pressed = (a[0] * count_a + b[0] * count_b, 
                    a[1] * count_a + b[1] * count_b)
    return pressed == prize, count_a * 3 + count_b * 1

def one(buttons_a, buttons_b, prizes):
    ans = 0
    for i in range(len(prizes)):
        possible, tokens = False, 400
        for x in range(100):
            for y in range(100):
                check, cost = is_answer(buttons_a[i], x, 
                                buttons_b[i], y, prizes[i])
                if check:
                    possible = True
                    tokens = min(tokens, cost)
        if possible:
            ans += tokens
    return ans

def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q = a // b
        a, b = b, a - q * b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def lcm(a, b):
    return a * b // find_gcd(a, b)

def solve_eq(a1, a2, b1, b2, p1, p2):
    k2 = (p1*a2 - p2*a1) // (b1*a2 - b2*a1)
    k1 = (p1 - b1*k2) // a1
    return k1, k2

def two(buttons_a, buttons_b, prizes):
    ans = 0
    for i in range(len(prizes)):
        gcd_x = find_gcd(buttons_a[i][0], buttons_b[i][0])
        prizes[i] = (prizes[i][0] + 10000000000000, prizes[i][1] + 10000000000000)
        if prizes[i][0] % gcd_x != 0:
            continue
        gcd_y = find_gcd(buttons_a[i][1], buttons_b[i][1])
        if prizes[i][1] % gcd_y != 0:
            continue
        
        k1, k2 = solve_eq(buttons_a[i][0], buttons_a[i][1],
                        buttons_b[i][0], buttons_b[i][1],
                        prizes[i][0], prizes[i][1])
        solved, count = is_answer(buttons_a[i], k1, buttons_b[i], k2, prizes[i])
        if solved:
            ans += count
        
    return ans


fin = open('d13_in.txt', 'r')
fout = open('d13_out.txt', 'w')

lines = fin.readlines()
buttons_a, buttons_b, prizes = parse(lines)

fout.write(str(two(buttons_a, buttons_b, prizes)))

fin.close()
fout.close()
