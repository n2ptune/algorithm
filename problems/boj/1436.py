def find_number(x):
  try:
    return str(x).index('666')
  except:
    return -1


ans = []
i = 666
inp = int(input())

while len(ans) < inp:
  if find_number(i) != -1:
    ans.append(i)
  i += 1

print(ans[inp - 1])