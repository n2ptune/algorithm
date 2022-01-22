fn main() {
    let ans: i32 = {
        let mut burger: i32 = 0;
        let mut drink: i32 = 0;

        for i in 0..5 {
            let mut s = String::new();
            std::io::stdin().read_line(&mut s);
            let price: i32 = s.trim().parse::<i32>().unwrap();
            if i >= 3 {
                if drink == 0 {
                    drink = price;
                }
                if drink > price {
                    drink = price;
                }
            } else {
                if burger == 0 {
                    burger = price;
                }
                if burger > price {
                    burger = price;
                }
            }
        }

        (burger + drink) - 50
    };

    println!("{}", ans);
}
