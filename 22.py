def parse(lines):
    secrets = []
    for line in lines:
        if line:
            secrets.append(int(line.strip()))
    return secrets

M = 1 << 24

def next_secret(number):
    n1 = ((number << 6) ^ number) % M
    n2 = ((n1 >> 5) ^ n1) % M
    n3 = ((n2 << 11) ^ n2) % M
    return n3

def one(secrets):
    max_next = 2000
    ans = 0
    for secret in secrets:
        for i in range(max_next):
            secret = next_secret(secret)
        ans += secret
    return ans

def two():
    pass

fin = open('d22_in.txt', 'r')
fout = open('d22_out.txt', 'w')

lines = fin.readlines()
secrets = parse(lines)

fout.write(str(one(secrets)))

fin.close()
fout.close()
