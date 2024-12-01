def one(left, right):
    left.sort()
    right.sort()

    ans = sum([abs(x - y) for x,y in zip(left, right)])
    return ans

def two(left, right):
    left.sort()
    right.sort()
    ans = 0
    r = 0
    for x in left:
        while r < len(right) and right[r] < x:
            r += 1
        r1 = r
        while r1 < len(right) and right[r1] == x:
            r1 += 1
        ans += x * (r1 - r)
    return ans

fin = open('d1_in.txt', 'r')
fout = open('d1_out.txt', 'w')

lines = fin.readlines()
left, right = [], []
for l in lines:
    a, b = l.split()
    left.append(int(a))
    right.append(int(b))

fout.write(str(two(left, right)))

fin.close()
fout.close()
