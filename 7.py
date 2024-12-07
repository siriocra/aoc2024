def parse(lines):
    results, numbers = [], []
    for line in lines:
        res, nums = line.split(':')
        nums = list(map(int, nums.strip().split()))
        results.append(int(res))
        numbers.append(nums)
    return results, numbers

def try_op(res, nums, concat=False):
    if len(nums) == 1:
        return res == nums[0]
    a, b = nums[-1], nums[-2]
    nums.pop()
    nums[-1] = a * b
    success = try_op(res, nums, concat)
    if not success:
        nums[-1] = a + b
        success = try_op(res, nums, concat)
    if concat and not success:
        nums[-1] = int(str(a) + str(b))
        success = try_op(res, nums, concat)
    nums[-1] = b
    nums.append(a)
    return success
    

def one(results, numbers):
    ans = 0
    for res, nums in zip(results, numbers):
        nums.reverse()
        success = try_op(res, nums)
        if success:
            ans += res
    return ans


def two(results, numbers):
    ans = 0
    for res, nums in zip(results, numbers):
        nums.reverse()
        success = try_op(res, nums, concat=True)
        if success:
            ans += res
    return ans

fin = open('d7_in.txt', 'r')
fout = open('d7_out.txt', 'w')

lines = fin.readlines()
results, numbers = parse(lines)

fout.write(str(two(results, numbers)))

fin.close()
fout.close()
