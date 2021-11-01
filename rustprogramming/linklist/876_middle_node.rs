// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode {
            next: None,
            val
        }
    }
}

struct Solution;

impl Solution {
    pub fn middle_node(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut slow = &head;
        let mut fast = &head;
        while fast.is_some() && fast.as_ref().unwrap().next.is_some() {
            slow = &slow.as_ref().unwrap().next;
            fast = &fast.as_ref().unwrap().next;
            fast = &fast.as_ref().unwrap().next;
        }
        return slow.clone();
    }
}

fn main() {
    let node1 = Some(Box::new(ListNode { 
		val: 1,
		next: Some(Box::new(ListNode {
			val: 2,
			next: Some(Box::new(ListNode {
				val: 3,
				next: None,
			}))
		}))
    }));
    println!("{:?}", Solution::middle_node(node1));
}