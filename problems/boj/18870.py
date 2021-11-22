import sys
read = sys.stdin.readline

_ = int(read())
nm = list(map(int, read().split(' ')))
dnm = list(sorted(dict.fromkeys(nm)))
di = { dnm[i]: i for i in range(len(dnm)) }
ans = [di[i] for i in nm]
print(' '.join(map(str, ans)))
