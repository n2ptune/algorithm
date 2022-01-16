use std::collections::HashMap;

fn main() {
    let mut t = String::new();
    let mut input = String::new();
    std::io::stdin().read_line(&mut t).unwrap();
    std::io::stdin().read_line(&mut input).unwrap();
    let v: Vec<&str> = input.split_whitespace().collect();

    let mut hash: HashMap<&str, i32> = HashMap::new();

    for ch in v {
        hash.insert(ch, 1);
    }

    let mut mt = String::new();
    let mut mn = String::new();
    std::io::stdin().read_line(&mut mt).unwrap();
    std::io::stdin().read_line(&mut mn).unwrap();
    let b: Vec<&str> = mn.split_whitespace().collect();

    for ch in b {
        match hash.get(ch) {
            None => println!("0"),
            Some(_) => println!("1"),
        }
    }
}
