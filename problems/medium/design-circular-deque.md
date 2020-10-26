| Time Submmited   | Status   | Runtime | Memory  | Language   |
| ---------------- | -------- | ------- | ------- | ---------- |
| 10/27/2020 02:43 | Accepted | 136 ms  | 46.1 MB | javascript |

## 641. Design Circular Deque

원문: [641. Design Circular Deque](https://leetcode.com/problems/design-circular-deque/)

**Deque**를 설계하면 된다. 따로 클래스로 만들어도 되지만 답안지에 시그니쳐가 이미 작성되어 있어 재작성하지 않고 그대로의 것을 사용했다.

**Deque**는 양쪽 끝에서 삽입과 삭제가 모두 가능한 자료구조이다. 큐와 스택을 합친 형태라고 생각하면 이해하기 쉽다. 문제에서는 아래와 같은 메소드를 구현하면 된다.

- 덱 앞에 값을 넣는 `insertFront` 메소드
- 덱 끝에 값을 넣는 `insertLast` 메소드
- 덱 앞의 값을 삭제하는 `deleteFront` 메소드
- 덱 끝의 값을 삭제하는 'deleteLast` 메소드
- 덱 앞의 값을 가져오는 `getFront` 메소드
- 덱 끝의 값을 가져오는 `getRear` 메소드
- 덱이 비어있는지 확인하는 `isEmpty` 메소드
- 덱이 꽉 찼는지 확인하는 `isFull` 메소드

삽입과 삭제는 모두 동작이 끝나고 성공적으로 수행되면 `true`를 반환해야 한다. 그렇지 않은 경우에는 `false`를 반환하면 된다. 처음 **Deque**의 최대 길이를 입력받고 시작한다. 덱의 길이가 이 범위를 벗어나면 삽입이 되지 않는다.

문제는 구현해야 할 메소드를 나열된 순서 반대로 구현하면 나머지 메소드를 좀 더 편하게 구현할 수 있다. 삽입해야 하는 `insertXXX` 메소드는 덱의 길이가 꽉 찼는지 확인해야 하기 때문에, `isFull` 메소드가 선행되면 편하다.

반대로, 덱의 값을 삭제하는 `deleteXXX` 메소드는 덱이 비어있을 때 실행되면 안되기 때문에 `isEmpty`가 선행적으로 구현되면 편하다.

```js
/**
 * Initialize your data structure here. Set the size of the deque to be k.
 * @param {number} k
 */
var MyCircularDeque = function (k) {
  this.queue = []
  this.k = k
}

/**
 * Adds an item at the front of Deque. Return true if the operation is successful.
 * @param {number} value
 * @return {boolean}
 */
MyCircularDeque.prototype.insertFront = function (value) {
  if (this.isFull()) {
    return false
  }

  this.queue.unshift(value)
  return true
}

/**
 * Adds an item at the rear of Deque. Return true if the operation is successful.
 * @param {number} value
 * @return {boolean}
 */
MyCircularDeque.prototype.insertLast = function (value) {
  if (this.isFull()) {
    return false
  }

  this.queue.push(value)
  return true
}

/**
 * Deletes an item from the front of Deque. Return true if the operation is successful.
 * @return {boolean}
 */
MyCircularDeque.prototype.deleteFront = function () {
  if (this.isEmpty()) {
    return false
  }

  this.queue.shift()
  return true
}

/**
 * Deletes an item from the rear of Deque. Return true if the operation is successful.
 * @return {boolean}
 */
MyCircularDeque.prototype.deleteLast = function () {
  if (this.isEmpty()) {
    return false
  }

  this.queue.pop()
  return true
}

/**
 * Get the front item from the deque.
 * @return {number}
 */
MyCircularDeque.prototype.getFront = function () {
  return this.isEmpty() ? -1 : this.queue[0]
}

/**
 * Get the last item from the deque.
 * @return {number}
 */
MyCircularDeque.prototype.getRear = function () {
  return this.isEmpty() ? -1 : this.queue[this.queue.length - 1]
}

/**
 * Checks whether the circular deque is empty or not.
 * @return {boolean}
 */
MyCircularDeque.prototype.isEmpty = function () {
  return !!!this.queue.length
}

/**
 * Checks whether the circular deque is full or not.
 * @return {boolean}
 */
MyCircularDeque.prototype.isFull = function () {
  return this.queue.length >= this.k
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * var obj = new MyCircularDeque(k)
 * var param_1 = obj.insertFront(value)
 * var param_2 = obj.insertLast(value)
 * var param_3 = obj.deleteFront()
 * var param_4 = obj.deleteLast()
 * var param_5 = obj.getFront()
 * var param_6 = obj.getRear()
 * var param_7 = obj.isEmpty()
 * var param_8 = obj.isFull()
 */
```
