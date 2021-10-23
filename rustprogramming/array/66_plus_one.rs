struct Solution;


impl Solution {
    pub fn plus_one(digits: Vec<i32>) -> Vec<i32> {
        let mut result: Vec<i32> = digits.clone();

        for i in (0..result.len()).rev() {
            if result[i] == 9 {
                result[i] = 0;
            } else {
                result[i] += 1;
                break;
            }
        }

        if result[0] == 0 {
            result.push(0);
            result[0] = 1;
        }

        return result;
    }
}


fn main() {
    let digits = vec![1, 2, 3];
    println!("{:?}", Solution::plus_one(digits));

    let digits = vec![4, 3, 2, 1];
    println!("{:?}", Solution::plus_one(digits));

    let digits = vec![0];
    println!("{:?}", Solution::plus_one(digits));

    let digits = vec![9, 9];
    println!("{:?}", Solution::plus_one(digits));
}