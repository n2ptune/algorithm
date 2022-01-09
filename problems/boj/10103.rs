fn main() {
  let mut t: i32 = {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    
    s.trim().parse().unwrap()
  };

  let mut a = 100;
  let mut b = 100;
  
  for _ in 0..t {
    let tr: Vec<i32> = {
      let mut s = String::new();
      std::io::stdin().read_line(&mut s).unwrap();
      let trv: Vec<i32> = s.split_whitespace().map(|s| s.parse().unwrap()).collect();

      trv
    };

    if tr[0] > tr[1] {
      b = b - tr[0]
    } else if tr[1] > tr[0] {
      a = a - tr[1]
    }
  }

  println!("{}", a);
  println!("{}", b);
}