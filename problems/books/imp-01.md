## 왕실의 나이트

체스판에서 나이트는 L자 형태로만 이동이 가능합니다. 위치가 주어지면 나이트가 이동할 수 있는 모든 경우의 수를 구하는 문제입니다. 먼저 체스판의 열은 영어 알파벳 형태로 적혀있고 행은 1부터 숫자 8까지 총 8x8 형태의 체스판입니다.

나이트는 L자 형태로 움직이기 때문에 총 8개의 경우의 수로 움직일 수 있습니다. 그러므로 답은 8을 초과할 수 없고 계산해야 하는 경우의 수가 8가지이므로 제한 시간인 1초안에 문제를 풀 수 있습니다.

```py
x, y = list(input())
```

`x`와 `y`를 입력받습니다.

```py
x = ord(x) - 97
y = int(y) - 1
```

리스트를 쉽게 접근할 수 있게 `x`와 `y`를 `int` 타입으로 바꿔줍니다.

```py
d = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [1, -2], [-1, 2], [1, 2]]
```

나이트가 이동할 수 있는 `x` 값과 `y` 값을 리스트로 지정해줍니다.

```py
ans = 0

for dx, dy in d:
  if x + dx >= 0 and y + dy >= 0:
    ans += 1

print(ans)
```

`ans`에는 경우의 수를 카운트합니다. `d` 안의 `x` 값과 `y` 값을 반복해서 가져와 현재 위치와 더합니다. 더한 값 중에 마이너스가 되는 값이 있다면 체스판 바깥으로 벗어난 것이므로 경우의 수에 포함되지 않습니다. 그러므로 마이너스가 나오지 않을 때에만 변수를 카운트합니다.