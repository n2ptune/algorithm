T = int(input())
ans = []


def remove_duplicate(l):
  return [*set(l)]


for i in range(T):
  a, b, c = map(int, input().split(' '))
  no_dup = remove_duplicate([a, b, c])

  if len(no_dup) == 2:
    who_dup = 0
    for j in no_dup:
      if [a, b, c].count(j) > 1:
        who_dup = j
    ans.append(1000 + who_dup * 100)
  elif len(no_dup) == 3:
    top = sorted([a, b, c])[2]
    ans.append(top * 100)
  else:
    ans.append(10000 + a * 1000)

print(sorted(ans)[T - 1])