struct Solution;

impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        if nums.len() <= 1 {
            return nums.len() as i32;
        }
        let mut i: usize = 0;
        for j in 1..nums.len() {
            if nums[j] != nums[i] {
                nums[i + 1] = nums[j];
                i += 1;
            }
        }
        return (i + 1) as i32;
    }
}

fn main() {
    let mut nums: Vec<i32> = vec![];
    println!("{}", Solution::remove_duplicates(&mut nums));

    let mut nums: Vec<i32> = vec![1, 1, 2];
    println!("{}", Solution::remove_duplicates(&mut nums));

    let mut nums: Vec<i32> = vec![0, 0, 1, 1, 1, 2, 2, 3, 3, 4];
    println!("{}", Solution::remove_duplicates(&mut nums));
}