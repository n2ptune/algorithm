import sys
read = sys.stdin.readline

N = int(read())
nums = list(map(int, read().rstrip().split(' ')))

print(max(nums) - min(nums))