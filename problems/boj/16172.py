import sys
read = sys.stdin.readline


def toAlpha(x):
  if (ord(x) >= 65 and ord(x) <= 90) or (ord(x) >= 97 and ord(x) <= 122):
    return True
  else:
    return False


S = filter(toAlpha, list(read().rstrip()))
K = read().rstrip()
L = ''.join(list(S))

print(1 if not L.find(K) == -1 else 0)