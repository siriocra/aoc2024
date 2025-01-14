num_ways = {
    'A': {'A': [''], '0': ['<'], '1': ['^<<'], '2': ['^<', '<^'], '3': ['^'], '4': ['^^<<'], '5': ['^^<', '<^^'], '6': ['^^'], '7': ['^^^<<'], '8': ['<^^^', '^^^<'], '9': ['^^^']},
    '0': {'A': ['>'], '0': [''], '1': ['^<'], '2': ['^'], '3': ['^>', '>^'], '4': ['^^<'], '5': ['^^'], '6': ['^^>', '>^^'], '7': ['^^^<'], '8': ['^^^'], '9': ['^^^>', '>^^^']},
    '1': {'A': ['>>v'], '0': ['>v'], '1': [''], '2': ['>'], '3': ['>>'], '4': ['^'], '5':['>^', '^>'], '6': ['>>^', '^>>'], '7': ['^^'], '8': ['>^^', '^^>'], '9': ['>>^^', '^^>>']},
    '2': {'A': ['>v', 'v>'], '0': ['v'], '1': ['<'], '2': [''], '3': ['>'], '4': ['^<', '<^'], '5': ['^'], '6': ['^>', '>^'], '7': ['^^<', '<^^'], '8': ['^^'], '9': ['^^>', '>^^']},
    '3': {'A': ['v'], '0': ['v<', '<v'], '1': ['<<'], '2': ['<'], '3': [''], '4': ['^<<', '<<^'], '5': ['^<', '<^'], '6': ['^'], '7': ['<<^^', '^^<<'], '8': ['<^^', '^^<'], '9': ['^^']},
    '4': {'A': ['>>vv'], '0': ['>vv'], '1': ['v'], '2': ['>v', 'v>'], '3': ['>>v', 'v>>'], '4': [''], '5': ['>'], '6': ['>>'], '7': ['^'], '8': ['^>', '>^'], '9': ['^>>', '>>^']},
    '5': {'A': ['vv>', '>vv'], '0': ['vv'], '1': ['v<', '<v'], '2': ['v'], '3': ['v>', '>v'], '4': ['<'], '5': [''], '6': ['>'], '7': ['^<', '<^'], '8': ['^'], '9': ['^>', '>^']},
    '6': {'A': ['vv'], '0': ['vv<', '<vv'], '1': ['v<<', '<<v'], '2': ['v<', '<v'], '3': ['v'], '4': ['<<'], '5': ['<'], '6': [''], '7': ['^<<', '<<^'], '8': ['^<', '<^'], '9': ['^']},
    '7': {'A': ['>>vvv'], '0': ['>vvv'], '1': ['vv'], '2': ['>vv', 'vv>'], '3': ['vv>>', '>>vv'], '4': ['v'], '5': ['>v', 'v>'], '6': ['>>v', 'v>>'], '7': [''], '8': ['>'], '9': ['>>']},
    '8': {'A': ['vvv>', '>vvv'], '0': ['vvv'], '1': ['vv<', '<vv'], '2': ['vv'], '3': ['vv>', '>vv'], '4': ['<v', 'v<'], '5': ['v'], '6': ['v>', '>v'], '7': ['<'], '8': [''], '9': ['>']},
    '9': {'A': ['vvv'], '0': ['vvv<', '<vvv'], '1': ['vv<<', '<<vv'], '2': ['vv<', '<vv'], '3': ['vv'], '4': ['v<<', '<<v'], '5': ['v<', '<v'], '6': ['v'], '7': ['<<'], '8': ['<'], '9': ['']},
}

dir_ways = {
    'A': {'A': [''], '^': ['<'], '>': ['v'], 'v': ['v<', '<v'], '<': ['v<<']},
    '^': {'A': ['>'], '^': [''], '>': ['v>', '>v'], 'v': ['v'], '<': ['v<']},
    '<': {'A': ['>>^'], '^': ['>^'], '>': ['>>'], 'v': ['>'], '<': ['']},
    'v': {'A': ['>^', '^>'], '^': ['^'], '>': ['>'], 'v': [''], '<': ['<']},
    '>': {'A': ['^'], '^': ['^<', '<^'], '>': [''], 'v': ['<'], '<': ['<<']},
}

def parse(lines):
    nums = []
    for line in lines:
        if line:
            nums.append(line.strip())
    return nums

def dir_pad(pattern, depth):
    if depth == 0:
        return len(pattern)
    else:
        new_p = ''
        prev = 'A'
        for i in range(len(pattern)):
            new_p += dir_ways[prev][pattern[i]] + 'A'
            prev = pattern[i]
        return dir_pad(new_p, depth-1)

def num_pad(pattern, depth):
    new_p = ''
    prev = 'A'
    for i in range(len(pattern)):
        new_p += num_ways[prev][pattern[i]] + 'A'
        prev = pattern[i]
    return dir_pad(new_p, depth)

all_patterns = ('A', '<', '^', 'v', '>')
patterns_id = {'A': 0, '<': 1, '^': 2, 'v': 3, '>': 4}

def precalc_dir_pad(depth):
    patterns = [[[0] * len(all_patterns) for i in range(len(all_patterns))] for j in range(depth)]
    for i in range(len(all_patterns)):
        for j in range(len(all_patterns)):
            patterns[0][i][j] = len(dir_ways[all_patterns[i]][all_patterns[j]][0]) + 1
    for k in range(1, depth):
        for i in range(len(all_patterns)):
            for j in range(len(all_patterns)):
                patterns[k][i][j] = float('inf')
                for dir_pattern in dir_ways[all_patterns[i]][all_patterns[j]]:
                    patterns[k][i][j] = min(patterns[k][i][j],
                        calc_dir_pad(dir_pattern, patterns[k-1]))
    return patterns[-1]

def calc_dir_pad(pattern, patterns):
    ans = 0
    prev = 'A'
    for i in range(len(pattern)):
        ans += patterns[patterns_id[prev]][patterns_id[pattern[i]]]
        prev = pattern[i]
    ans += patterns[patterns_id[prev]][patterns_id['A']]
    return ans

def calc_num_pad(pattern, patterns):
    ans = 0
    prev = 'A'
    for i in range(len(pattern)):
        min_ans = float('inf')
        for dir_pattern in num_ways[prev][pattern[i]]:
            min_ans = min(min_ans, calc_dir_pad(dir_pattern, patterns))
        prev = pattern[i]
        ans += min_ans
    return ans

def one(nums):
    ans = 0
    for num in nums:
        ans += int(num[:-1]) * num_pad(num, 2)
    return ans

def two(nums):
    patterns = precalc_dir_pad(25)
    ans = 0
    for num in nums:
        print(calc_num_pad(num, patterns), num)
        ans += int(num[:-1]) * calc_num_pad(num, patterns)
    return ans

fin = open('d21_in.txt', 'r')
fout = open('d21_out.txt', 'w')

lines = fin.readlines()
nums = parse(lines)

fout.write(str(two(nums)))

fin.close()
fout.close()
