fn main() {
  let count: i32 = {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    let v: i32 = s.trim().parse().unwrap();
    v
  };
  
  for _ in 0..count {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();
    let splited: Vec<&str> = s.split_whitespace().collect();
    let mut current: f64 = splited[0].parse().unwrap();
    let commands = &splited[1..];

    for command in commands {
      let c: f64 = match command.as_ref() {
        "@" => 3.0,
        "%" => 5.0,
        "#" => -7.0,
        _ => 0.0,
      };
      if c == 3.0 {
        current = current * 3.00;
      } else {
        current += c;
      }
    }

    println!("{:.2}", current);
  }
}