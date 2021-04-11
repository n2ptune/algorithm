## 문자열

정해진 횟수만큼 문자열을 입력받고 해당 문자열의 제일 첫번째 문자와 마지막 문자를 출력하면 되는 문제이긴 한데 파이썬으로 작성하면 매우 쉽게 풀리지만 러스트로는 조금 생각을 해야 되는 부분이 있어서 시간이 걸린다.

### 숫자 입력받기

문자열을 입력받으려면 아래와 같이 하면 된다.

```rust
use std::io;

fn main() {
  let mut s = String::new();
  io::stdin().read_line(&mut s);
}
```

숫자를 입력받으려면 먼저 문자열로 입력받고 파싱하는 단계가 필요하다.

```rust
use std::io;

fn main() {
  let mut c = String::new();
  io::stdin().read_line(&mut c);
  let count: i32 = c.trim().parse().unwrap();
}
```

### 파싱한 숫자로 반복문 돌기

변환한 숫자 만큼 반복문을 돌릴 때 파이썬에서는 `range(N)`으로 쉽게 N번 반복할 수 있다. 러스트에서는 아래와 같이 할 수 있다.

```rust
use std::io;

fn main() {
  let mut c = String::new();
  io::stdin().read_line(&mut c);
  let count: i32 = c.trim().parse().unwrap();

  for i in 0..count {
    println!("{}", i);
  }
}
```

총 `count`번 반복문을 돌게 된다. 0에서 부터 count까지 변수 `i`에 값이 담기지만 count는 포함되지 않는다.

### 첫 문자, 마지막 문자 뽑기

러스트에서 문자열 인덱싱은 유효하지 않기 때문에 다른 방법을 사용해야한다. (각 문자당 차지하는 바이트 수가 다를 수 있기 때문에 인덱싱을 이용해서 해당 문자를 얻어낼 때 그 문자가 뽑아낸 문자와 동일하다는 걸 보장할 수 없다.)

문자열에서 문자들로 이루어진 반복 가능한 객체로 만들어주는 메서드 `chars`를 이용한다.

```rust
let first_char = ans.chars().next().unwrap();
```

마지막 문자는 위와 마찬가지로 `chars`로 문자를 뽑아서 리버스시킨다. 그러면 맨 마지막 문자가 제일 앞에 위치하게 된다.

```rust
let last_char = ans.trim_end().rev().next().unwrap();
```

마지막 문자에 줄바꿈 이스케이프 시퀀스가 포함될 수 있으니 제거해준다.

```rust
use std::io;

fn main() {
  let mut count = String::new();

  io::stdin().read_line(&mut count);

  let n: i32 = count.trim().parse().unwrap();

  for i in 0..n {
    let mut ans = String::new();
    io::stdin().read_line(&mut ans);

    let first_char = ans.chars().next().unwrap();
    let last_char = ans.trim_end().chars().rev().next().unwrap();
    println!("{}{}", first_char, last_char);
  }
}
```
