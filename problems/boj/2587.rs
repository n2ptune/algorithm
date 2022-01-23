fn main() {
    let ans: (i32, i32) = {
        let mut v: Vec<i32> = Vec::new();
        for _ in 0..5 {
            let mut s = String::new();
            std::io::stdin().read_line(&mut s).unwrap();
            v.push(s.trim().parse::<i32>().unwrap());
        }
        v.sort();
        let su: i32 = v.iter().sum();

        (su / 5, v[2])
    };

    println!("{}", ans.0);
    println!("{}", ans.1);
}
