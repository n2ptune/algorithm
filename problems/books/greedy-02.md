## 곱하기 혹은 더하기

제일 먼저 생각해야될 건 규칙성일 것 같습니다. 연산을 시도하려는 두 수 중 하나라도 0을 포함한다면 다른 수가 아무리 큰 수라도 곱해버리면 0이 되니 더해야합니다. 그리고 두 수 중 하나라도 1이라면 곱하기는 항상 제자리이기 때문에 더해야 제일 큰 수를 얻을 수 있습니다. 이 규칙을 제외하고는 모두 곱합니다. 그리고 이 문제에서는 사칙연산의 우선순위는 무시하고 왼쪽부터 순서대로 연산하므로 왼쪽부터 반복하면 됩니다.

길이가 1일 땐 더하거나 곱할 수가 없으므로 그 수가 제일 큰 수입니다. 길이가 2일 땐 두 수를 곱하거나 더한 수가 제일 큰 수입니다. 두 수가 들어오면 이걸 더할지, 곱할지 판단해주는 함수를 하나 만들고 제일 큰 수를 반환하게 합니다.

길이가 3 이상인 리스트에서는 먼저 첫번째 인덱스와 두번째 인덱스를 계산하고 저장해둡니다. 그리고 나머지 수들과 저장해둔 수와 더하거나 곱합니다. 이 행위를 리스트 끝까지 반복합니다.

```py
S = list(map(int, list(input())))


def calTwoNum(a, b):
  if a == 0 or b == 0:
    return a + b
  elif a == 1 or b == 1:
    return a + b
  else:
    return a * b


if len(S) == 1:
  print(S[0])
elif len(S) == 2:
  print(calTwoNum(S[0], S[1]))
else:
  C = calTwoNum(S[0], S[1])
  S = S[2:]

  for num in S:
    C = calTwoNum(C, num)

  print(C)
```