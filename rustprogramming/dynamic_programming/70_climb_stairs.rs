struct Solution;

impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        // let (mut dp0, mut dp1) = (1, 2);
        // for _ in 1..n {
        //     let tmp = dp0 + dp1;
        //     dp0 = dp1;
        //     dp1 = tmp;
        // }
        // return dp0;

        let mut fib = (1, 1);
        for _ in 0..n {
            fib = (fib.1, fib.0 + fib.1);
        }
        fib.0
    }
}

fn main() {
    println!("{}", Solution::climb_stairs(1));
    println!("{}", Solution::climb_stairs(2));
    println!("{}", Solution::climb_stairs(3));
}