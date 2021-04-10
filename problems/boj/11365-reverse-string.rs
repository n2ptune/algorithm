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