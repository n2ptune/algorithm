| Time Submmited   | Status   | Runtime | Memory  | Language   |
| ---------------- | -------- | ------- | ------- | ---------- |
| 09/26/2020 04:42 | Accepted | 96 ms   | 40.3 MB | javascript |

## 83. Remove Duplicates from Sorted List

원문: [83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

정렬된 리스트에서 중복을 제거하는 문제, 매우 간단한 문제이긴 하지만 생각을 좀 오래했던 것 같다. 먼저 매개변수로 온 리스트에 대한 참조를 하나 만들고 현재 리스트의 값과 다음 비교할 값인 `next`가 존재할 때까지 루프를 돈다.

맨 처음, 현재 노드 값과 `next` 값이 같다면 현재 리스트의 `next` 참조를 값이 같은 리스트의 `next`로 바꾼다. 그러면 일단 중복된 값을 한 개 지울 수 있다. 만약 비교하는 값이 다르다면, 중복이 아닌 경우이므로 현재 리스트의 `next`를 비교한 리스트로 둔다.

결과적으로 매개변수로 온 `head` 값을 반환한다.

```js
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function (head) {
  var h = head

  while (h && h.next) {
    if (h.val === h.next.val) {
      h.next = h.next.next
    } else {
      h = h.next
    }
  }

  return head
}
```
