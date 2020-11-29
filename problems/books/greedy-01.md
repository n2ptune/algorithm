## 모험가 길드

모험가의 정보를 모두 입력받고 오름차순으로 정렬합니다. 먼저 정렬하게 되면 최소한의 그룹 인원으로 그룹을 구성할 수 있으며 문제에서 요구하는 최대 그룹 수를 구할 수 있습니다. 그룹 수를 카운트하기 위해 `group_count` 변수와 현재 그룹의 명 수를 담기위해 변수 `group`을 선언하고 0으로 초기화합니다.

모든 모험가를 반복하고 `group`에 1씩 더합니다. 만약 현재 모험가의 공포도가 그룹 수와 동일하다면 그룹이 결성됬으므로 `group_count`를 하나 늘리고 `group`을 다시 0으로 초기화합니다.

```python
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
```
