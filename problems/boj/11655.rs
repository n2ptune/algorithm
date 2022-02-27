use std::io;
use std::char;

fn main() {
  let mut st = String::new();
  let mut convert = String::new();

  io::stdin().read_line(&mut st);

  for c in st.trim_end().chars() {
    let mut p = c as u32;

    if p >= 65 && p <= 90 {
      p += 13;
      if p > 90 {
        let temp: u32 = p - 90;
        p = 64 + temp;
      }
    } else if p >= 97 && p <= 122 {
      p += 13;
      if p > 122 {
        let temp: u32 = p - 122;
        p = 96 + temp;
      }
    }

    convert.push(char::from_u32(p).unwrap());
  }

  println!("{}", convert);
}