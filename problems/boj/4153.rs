fn main() {
  loop {
    let mut s = String::new();

    std::io::stdin().read_line(&mut s).unwrap();

    let v: Vec<i32> = s.split_whitespace().map(|s| s.parse().unwrap()).collect();
    let b: Vec<i32> = v.iter().map(|s| s.pow(2)).collect();

    let f: Vec<i32> = v.into_iter().filter(|s| *s == 0).collect();

    if f.len() == 3 {
      break;
    }

    if b[0] + b[1] == b[2] {
      println!("right");
    } else {
      println!("wrong");
    }
  }
}