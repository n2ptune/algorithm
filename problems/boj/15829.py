import sys
l, s = sys.stdin.buffer.read().splitlines()
res = [(ch - 96) * (31 ** i ) for i, ch in enumerate(s)]

print(sum(res) % 1234567891)