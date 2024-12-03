import re

mulre = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
dore = r'do\(\)'
dontre = r'don\'t\(\)'
change = re.compile('(' + dore + '|' + dontre + ')')

def one(lines):
    ans = 0
    for line in lines:
        matches = re.findall(mulre, line)
        for a, b in matches:
            ans += int(a) * int(b)
    return ans

def two(lines):
    ans = 0
    enabled = True
    for line in lines:
        c = re.split(change, line)
        for word in c:
            if re.match(dore, word):
                enabled = True
            elif re.match(dontre, word):
                enabled = False
            else:
                if enabled:
                    ans += one([word])
    return ans

fin = open('d3_in.txt', 'r')
fout = open('d3_out.txt', 'w')

lines = fin.readlines()

fout.write(str(two(lines)))

fin.close()
fout.close()
