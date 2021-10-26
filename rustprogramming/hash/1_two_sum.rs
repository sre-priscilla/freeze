use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map: HashMap<i32, usize> = HashMap::new();
        for i in 0..nums.len() {
            if map.contains_key(&nums[i]) {
                let last_index = map[&nums[i]];
                return vec![last_index as i32, i as i32];
            }
            map.insert(target - nums[i], i);
        }
        return vec![];
    }
}

fn main() {
    println!("{:?}", Solution::two_sum(vec![2, 7, 11, 15], 9));
    println!("{:?}", Solution::two_sum(vec![3, 2, 4], 6));
    println!("{:?}", Solution::two_sum(vec![3, 3], 6));
}