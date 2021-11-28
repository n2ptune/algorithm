c = [0 for _ in range(26)]
s = input()

for ch in s:
  c[ord(ch) - 97] += 1
  
print(' '.join(list(map(str, c))))