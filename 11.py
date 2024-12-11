def parse(lines):
    return list(map(int, lines[0].strip().split()))

def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            mid = len(str(stone)) // 2
            a, b = int(str(stone)[:mid]), int(str(stone)[mid:])
            new_stones.append(a)
            new_stones.append(b)
        else:
            new_stones.append(stone * 2024)
    return new_stones

def blink_n(stone, n, cache):
    if n == 0:
        return 1
    if stone in cache[n]:
        return cache[n][stone]
    ans = 0
    if stone == 0:
        ans = blink_n(1, n-1, cache)
    elif len(str(stone)) % 2 == 0:
        mid = len(str(stone)) // 2
        a, b = int(str(stone)[:mid]), int(str(stone)[mid:])
        ans = blink_n(a, n-1, cache) + blink_n(b, n-1, cache)
    else:
        ans = blink_n(stone*2024, n-1, cache)
    cache[n][stone] = ans
    return ans


def one(stones):
    n = 25
    for i in range(n):
        stones = blink(stones)
    return len(stones)

def two(stones):
    n = 75
    ans = 0
    cache = [{} for i in range(n+1)]
    for stone in stones:
        ans += blink_n(stone, n, cache)
    return ans

fin = open('d11_in.txt', 'r')
fout = open('d11_out.txt', 'w')

lines = fin.readlines()
stones = parse(lines)

fout.write(str(two(stones)))

fin.close()
fout.close()
