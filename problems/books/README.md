# 이것이 취업을 위한 코딩테스트다 With 파이썬

책에 나오는 기출문제를 풀고 어떻게 풀었는지 나중에 복습하기 위해 그리고 푼 문제를 한번 더 보고 더 좋은 방법을 찾기 위해 기록합니다. 아래 문제들의 해설은 전부 주관적이며 정답 페이지를 보고 적은 해설이 아니기 때문에 정확하지 않을 수 있습니다.

## 목차

- [그리디 문제 01 모험가 길드](./greedy-01.md)

## 문제 풀이

각 문제들을 어떻게 풀었는지를 작성합니다.

### 그리디

> 현재 상황에서 가장 좋아 보이는 것만을 선택하는 알고리즘입니다. 현재 상황에서 가장 좋아 보이는 것만을 선택하기 때문에, 정확한 답을 도출하지 못하더라도 그럴싸한 답을 도출하는 데에 도움이 됩니다. 하지만 코딩 테스트에서는 대부분 '최적의 해'를 찾는 문제가 출제되기 때문에 그리디 알고리즘의 정당성을 고민하면서 문제 해결 방안을 떠올려야 합니다.

#### 모험가 길드

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