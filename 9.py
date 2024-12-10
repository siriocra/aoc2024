def parse(line):
    cur = 0
    pos = 0
    files, spaces, f_start, s_start = [], [], [], []
    for c in lines[0].strip():
        if cur % 2 == 0:
            files.append(int(c))
            f_start.append(pos)
        else:
            spaces.append(int(c))
            s_start.append(pos)
        pos += int(c)
        cur += 1
    return files, spaces, f_start, s_start

def calc_checksum(i, count, file_id):
    checksum = ((i + count) * (i + count - 1) - i * (i - 1)) // 2
    # print(i, file_id, count, checksum, checksum * file_id)
    return checksum * file_id

def defragment(files, spaces, f_start, s_start):
    ans = 0
    file_id = len(files) - 1
    checksum = 0
    for i in range(len(spaces)):
        pos = s_start[i]
        while spaces[i] > 0:
            if pos > f_start[file_id]:
                break
            moved = min(spaces[i], files[file_id])
            spaces[i] -= moved
            files[file_id] -= moved
            checksum += calc_checksum(pos, moved, file_id)
            pos += moved
            if files[file_id] == 0:
                file_id -= 1
    for i in range(len(files)):
        checksum += calc_checksum(f_start[i], files[i], i)
    return checksum

def one(files, spaces, f_start, s_start):
    return defragment(files, spaces, f_start, s_start)

def two(files, spaces, f_start, s_start):
    checksum = 0
    for file_id in range(len(files)-1, 0, -1):
        for space_id in range(len(spaces)):
            if f_start[file_id] < s_start[space_id]:
                checksum += calc_checksum(f_start[file_id], files[file_id], file_id)
                break
            if spaces[space_id] >= files[file_id]:
                spaces[space_id] -= files[file_id]
                checksum += calc_checksum(s_start[space_id], files[file_id], file_id)
                s_start[space_id] += files[file_id]
                break
    return checksum


fin = open('d9_in.txt', 'r')
fout = open('d9_out.txt', 'w')

lines = fin.readlines()
files, spaces, f_start, s_start = parse(lines)

fout.write(str(two(files, spaces, f_start, s_start)))

fin.close()
fout.close()
