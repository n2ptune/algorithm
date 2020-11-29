# 311 페이지 그리디 문제 모험가 길드
N = int(input())
people = list(map(int, input().split()))
people.sort()
group_count = 0
group = 0

for p in people:
  group += 1

  if group >= p:
    group_count += 1
    group = 0

print(group_count)