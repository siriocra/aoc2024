from collections import defaultdict

class TreeNode:
    def __init__(self, data, end=False):
        self.data = data
        self.end = end
        self.children = {}

    def add_child(self, letter, child):
        self.children[letter] = child

    def has_child(self, letter):
        if letter in self.children:
            return self.children[letter]
        else:
            return None

    def set_end(self, end):
        self.end = end

def parse(lines):
    towels = lines[0].strip().split(', ')
    patterns = []
    for line in lines[2:]:
        patterns.append(line.strip())
    return towels, patterns

def check_exists(root, node, pattern, cache):
    # print(root, node, pattern)
    if not pattern:
        return node.end
    if node == root and pattern in cache:
        return cache[pattern]
    child = node.has_child(pattern[0])
    check = 0
    if child:
        check += check_exists(root, child, pattern[1:], cache)
        if check > 0  and node == root:
            cache[pattern] += check
    if node.end and node != root:
        check += check_exists(root, root, pattern, cache)
    if check == 0 and node == root:
        cache[pattern] = 0
    return check

def create_tree(towels):
    root = TreeNode(None, True)
    for j in range(len(towels)):
        towel = towels[j]
        node = root
        for i in range(len(towel)-1):
            child = node.has_child(towel[i])
            if not child:
                child = TreeNode(j, False)
                node.add_child(towel[i], child)
            node = child
        last = node.has_child(towel[-1])
        if not last:
            child = TreeNode(j, True)
            node.add_child(towel[-1], child)
        else:
            last.set_end(True)
    return root

def one(towels, patterns):
    root = create_tree(towels)
    ans = 0
    cache = defaultdict(int)
    for pattern in patterns:
        if check_exists(root, root, pattern, cache) > 0:
            ans += 1
    return ans

def two(towels, patterns):
    root = create_tree(towels)
    ans = 0
    cache = defaultdict(int)
    for pattern in patterns:
        res = check_exists(root, root, pattern, cache)
        if res > 0:
            ans += res
    return ans

fin = open('d19_in.txt', 'r')
fout = open('d19_out.txt', 'w')

lines = fin.readlines()
towels, patterns = parse(lines)

fout.write(str(two(towels, patterns)))

fin.close()
fout.close()
