fn main() {
  let mut s = String::new();

  std::io::stdin().read_line(&mut s).unwrap();

  let v: i32 = s.trim().parse().unwrap();

  for __ in 0..v {
    let mut y: i32 = 0;
    let mut g: i32 = 0;

    for _ in 0..9 {
      let mut m = String::new();

      std::io::stdin().read_line(&mut m).unwrap();
  
      let o: Vec<i32> = m.split_whitespace().map(|s| s.parse().unwrap()).collect();
  
      y = y + o[0];
      g = g + o[1];
    }

    if y > g {
      println!("Yonsei");
    } else if g > y {
      println!("Korea");
    } else {
      println!("Draw");
    }
  }
}