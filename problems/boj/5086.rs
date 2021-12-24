use std::io;

fn main() {
  while (true) {
    let mut line = String::new();
    io::stdin().read_line(&mut line);
    let nums = line.trim().split(" ").flat_map(str::parse::<i32>).collect::<Vec<_>>();
    let a = nums[0];
    let b = nums[1];

    if a == 0 && b == 0 {
      break;
    } else if b % a == 0 {
      println!("factor");
    } else if a % b == 0 {
      println!("multiple");
    } else {
      println!("neither");
    }
  }
}