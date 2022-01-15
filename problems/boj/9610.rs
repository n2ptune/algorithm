fn main() {
    let answer: Vec<i32> = {
        let mut s = String::new();
        std::io::stdin().read_line(&mut s).unwrap();

        let count: i32 = s.trim().parse().unwrap();
        let mut ans: Vec<i32> = vec![0, 0, 0, 0, 0];

        for _ in 0..count {
            let mut sa = String::new();
            std::io::stdin().read_line(&mut sa).unwrap();

            let location: Vec<i32> = sa.split_whitespace().map(|s| s.parse().unwrap()).collect();

            if location[0] == 0 || location[1] == 0 {
                ans[4] += 1;
            }

            if location[0] > 0 && location[1] > 0 {
                ans[0] += 1;
            } else if location[0] < 0 && location[1] > 0 {
                ans[1] += 1;
            } else if location[0] < 0 && location[1] < 0 {
                ans[2] += 1;
            } else if location[0] > 0 && location[1] < 0 {
                ans[3] += 1;
            }
        }
        ans
    };

    for i in 1..5 {
        println!("Q{}: {}", i, answer[i - 1]);
    }
    println!("AXIS: {}", answer[answer.len() - 1])
}
