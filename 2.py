def safe(a):
    not_safe = 0
    if a[-1] < a[0]:
        a.reverse()
    for i in range(1, len(a)):
        if a[i] - a[i-1] < 1 or a[i] - a[i-1] > 3:
            not_safe += 1
    return not_safe

def one(reports):
    ans = 0
    for report in reports:
        if report and safe(report) == 0:
            ans += 1
    return ans

def two(reports):
    ans = 0
    for report in reports:
        for i in range(len(report)):
            new_report = report[:i] + report[i+1:]
            if new_report and safe(new_report) == 0:
                ans += 1
                break
    return ans

fin = open('d2_in.txt', 'r')
fout = open('d2_out.txt', 'w')

lines = fin.readlines()
reports = [list(map(int, l.split())) for l in lines]

fout.write(str(two(reports)))

fin.close()
fout.close()
