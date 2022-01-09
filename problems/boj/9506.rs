// temp
fn main() {
    loop {
        let t: i32 = {
            let mut s = String::new();
            std::io::stdin().read_line(&mut s).unwrap();
            s.trim().parse::<i32>().unwrap()
        };
        if t == -1 {
            break;
        }
        let mut v: Vec<i32> = Vec::new();
        let half: i32 = t / 2 + 1;
        for i in 1..half {
            if t % i == 0 {
                v.push(i);
            }
        }
        let sum: i32 = v.iter().sum();
        if sum > t || sum != t {
            println!("{} is NOT perfect.", t);
        } else {
            let joined: Vec<String> = v.iter().map(|&s| s.to_string()).collect();
            println!("{} = {:?}", t, joined.join(" + "));
        }
    }
}
