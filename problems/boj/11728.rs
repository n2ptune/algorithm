fn main() {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s);

    s = String::new();
    std::io::stdin().read_line(&mut s);

    let mut a: Vec<i32> = s
        .trim()
        .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();

    s = String::new();
    std::io::stdin().read_line(&mut s);

    let b: Vec<i32> = s
        .trim()
        .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();

    a.extend(&b);
    a.sort();

    let ans: Vec<String> = a.iter().clone().map(|s| s.to_string()).collect();

    println!("{}", ans.join(" "));
}
