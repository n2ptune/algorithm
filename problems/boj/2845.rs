use std::io;

fn main() {
  let mut s = String::new();

  io::stdin().read_line(&mut s).unwrap();

  let q: Vec<i32> = s.split_whitespace().map(|s| s.parse().unwrap()).collect();
  let mix: i32 = q[0] * q[1];

  s = String::new();

  io::stdin().read_line(&mut s).unwrap();

  let al: Vec<i32> = s.split_whitespace().map(|s| s.parse::<i32>().unwrap() - mix).collect();
  let xl: Vec<String> = al.iter().map(|&s| s.to_string()).collect();
  
  for x in xl {
    print!("{} ", x);
  }
}