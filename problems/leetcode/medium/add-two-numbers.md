| Time Submmited   | Status   | Runtime | Memory  | Language |
| ---------------- | -------- | ------- | ------- | -------- |
| 12/22/2020 18:21 | Accepted | 76 ms   | 14.4 MB | python3  |

## 2. Add Two Numbers

원문: [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

2개의 연결 리스트가 주어진다. 연결 리스트의 길이는 최대 100이고 각 노드의 값은 9보다 크지않은 값이다. 연결 리스트의 모든 노드는 역순으로 저장된 숫자다. 즉 `7 -> 1 -> 2` 연결 리스트는 `[2, 1, 7]`과 같다.

문제에서 원하는 답은 두 연결 리스트 노드들을 더한 값이다. 숫자가 역순으로 저장되었기 때문에 다른 처리가 필요할 것 같다. 여기에서는 연결 리스트의 값들을 파이썬 리스트로 모두 담아 합친 다음 정수로 변환한 후에 두 값을 더하고 다시 뒤집는 걸로 생각했다.

```py
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
  a = []
  b = []

  while l1:
    a.append(str(l1.val))
    l1 = l1.next
  while l2:
    b.append(str(l2.val))
    l2 = l2.next
```

`l1`과 `l2`는 각각 더해야 할 연결 리스트다. 두 연결 리스트를 순회해서 값만 리스트에 담아준다.

```py
a.reverse()
b.reverse()

c = int(''.join(a)) + int(''.join(b))
s = list((reversed(list(str(c)))))
```

두 배열을 뒤집고 뒤집은 값들을 합친 다음 정수로 변환하여 더한다. 그 값들을 다시 리스트로 변환한 뒤에 뒤집는다.

```py
ans = n = ListNode(s[0])

  if len(s) > 1:
    for item in s[1:]:
      n.next = ListNode(item)
      n = n.next
```

답은 연결 리스트로 반환해야 한다. 연결 리스트를 만드는 작업을 해준다. 첫번째 값으로 연결 리스트를 초기화하고 `ans`와 `n`에 모두 담는다. 두 변수는 같은 인스턴스를 가르킨다. 반환해야 하는 연결 리스트가 전체 연결 리스트를 반환해야 하므로 한 변수에서 연결 리스트를 만들 수 없다. 그래서 `ans`와 `n`을 두 개 사용한다.

첫번째 값을 담았으므로 두번째 값부터 연결 리스트에 담아야하는데, 리스트의 길이가 1을 초과할 때에만 반복문을 실행한다. (리스트 범위 초과) 연결 리스트에 모든 값을 담고 반환한다.
