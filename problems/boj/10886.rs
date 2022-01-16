fn main() {
    let is_cute: i32 = {
        let mut s = String::new();
        std::io::stdin().read_line(&mut s).unwrap();
        let c: i32 = s.trim().parse().unwrap();
        let mut cute = 0;
        let mut no_cute = 0;

        for _ in 0..c {
            s = String::new();
            std::io::stdin().read_line(&mut s).unwrap();
            let result: i32 = s.trim().parse().unwrap();

            if result == 1 {
                cute += 1;
            } else {
                no_cute += 1;
            }
        }

        if cute > no_cute {
            1
        } else {
            0
        }
    };

    if is_cute == 1 {
        println!("Junhee is cute!")
    } else {
        println!("Junhee is not cute!")
    }
}
