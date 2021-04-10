## !밀비 급일

제목에서 보면 알 수 있듯 문자열을 뒤집는 문제이다. 무한 루프를 돌다 빠져나가는 조건은 `END`가 입력될 때로 잡고 문자열을 입력받고 거꾸로 출력하면 된다.

```rust
use std::io;

fn main() {
  loop {
    let mut buf = String::new();
    io::stdin().read_line(&mut buf).unwrap();

    if buf.trim_end() == "END" {
      break;
    }

    println!("{}", buf.trim_end().chars().rev().collect::<String>());
  }
}
```
