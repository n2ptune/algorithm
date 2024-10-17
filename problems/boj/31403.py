import sys
a, b, c = map(int, sys.stdin.buffer.read().splitlines())
d, e, f = map(str, [a, b, c])

print('{0} {1}'.format(a + b - c, int(d + e) - int(f)))