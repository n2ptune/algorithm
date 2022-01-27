fn main() {
    let mut s = String::new();
    std::io::stdin().read_line(&mut s).unwrap();

    let mut temp: char = '?';
    let mut ans: i32 = 0;

    for ch in s.trim().chars() {
        if ch == '(' && temp == '(' {
            ans += 5;
        } else if ch == '(' && temp == ')' {
            ans += 10;
        } else if ch == ')' && temp == '(' {
            ans += 10;
        } else if temp == '?' {
            ans += 10;
        } else {
            ans += 5;
        }
        temp = ch;
    }

    println!("{}", ans);
}
