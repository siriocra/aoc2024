from collections import defaultdict

def parse(lines):
    graph = defaultdict(list)
    requests = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if '|' in line:
            a, b = map(int, line.split('|'))
            graph[b].append(a)
        else:
            requests.append(list(map(int, line.split(','))))
    return graph, requests

def dfs(x, graph, visited, request, order):
    visited[x] = True
    for y in graph[x]:
        if not visited[y] and y in request:
            dfs(y, graph, visited, request, order)
    order.append(x)

def middle(l):
    return l[len(l)//2]

def check_valid(request, graph):
    visited = [False] * 100
    order = []
    valid = True
    for page in request:
        if visited[page]:
            valid = False
        else:
            dfs(page, graph, visited, request, order)
    return valid, order

def one(graph, requests):
    ans = 0
    for request in requests:
        valid, _ = check_valid(request, graph)
        if valid:
            ans += middle(request)
    return ans


def two(graph, requests):
    ans = 0
    for request in requests:
        valid, order = check_valid(request, graph)
        if not valid:
            ans += middle(order)
    return ans

fin = open('d5_in.txt', 'r')
fout = open('d5_out.txt', 'w')

lines = fin.readlines()

graph, requests = parse(lines)

fout.write(str(two(graph, requests)))

fin.close()
fout.close()
