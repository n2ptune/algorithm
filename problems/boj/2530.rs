use std::io;

fn main() {
  let mut s = String::new();
  
  io::stdin().read_line(&mut s).unwrap();

  let q: Vec<i32> = s.split_whitespace().map(|s| s.parse().unwrap()).collect();
  let mut hour: i32 = q[0];
  let mut minute: i32 = q[1];
  let mut seconds: i32 = q[2];
  let day: i32 = (hour * 3600) + (minute * 60) + seconds;
  
  s = String::new();

  io::stdin().read_line(&mut s).unwrap();

  let z: i32 = s.trim().parse().unwrap();
  let mut ans: i32 = 0;
  let mut temp: i32 = 0;

  if z + day >= 86400 {
    ans = (z + day) - 86400;
    while ans >= 86400 {
      ans = ans - 86400;
    }
  } else {
    ans = z + day;
  }

  hour = ans / 3600;
  temp = ans % 3600;
  minute = temp / 60;
  temp = temp % 60;
  seconds = temp;

  println!("{} {} {}", hour, minute, seconds);
}