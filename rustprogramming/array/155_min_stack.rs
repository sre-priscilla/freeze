struct MinStack {
    nums_stack: Vec<i32>,
    mins_stack: Vec<i32>,
}

// impl MinStack {

//     fn new() -> Self {
//         MinStack {
//             nums_stack: Vec::new(),
//             mins_stack: Vec::new(),
//         }
//     }
    
//     fn push(&mut self, val: i32) {
//         self.nums_stack.push(val);
//         if self.mins_stack.is_empty() || val <= *self.mins_stack.last().unwrap() {
//             self.mins_stack.push(val)
//         }
//     }
    
//     fn pop(&mut self) {
//         if self.mins_stack.is_empty() {
//             return;
//         }
//         if self.nums_stack.pop().unwrap() == *self.mins_stack.last().unwrap() {
//             self.mins_stack.pop();
//         }
//     }
    
//     fn top(&self) -> i32 {
//         return *self.nums_stack.last().unwrap();
//     }
    
//     fn get_min(&self) -> i32 {
//         return *self.mins_stack.last().unwrap();
//     }
// }

impl MinStack {

    fn new() -> Self {
        MinStack {
            nums_stack: Vec::new(),
            mins_stack: Vec::new(),
        }
    }
    
    fn push(&mut self, val: i32) {
        self.nums_stack.push(val);
        if self.mins_stack.is_empty() {
            self.mins_stack.push(val);
        } else {
            let last_min = *self.mins_stack.last().unwrap();
            self.mins_stack.push(std::cmp::min(val, last_min));
        } 
    }
    
    fn pop(&mut self) {
        self.nums_stack.pop();
        self.mins_stack.pop();
    }
    
    fn top(&self) -> i32 {
        return *self.nums_stack.last().unwrap();
    }
    
    fn get_min(&self) -> i32 {
        return *self.mins_stack.last().unwrap();
    }
}

fn main() {
    let mut obj = MinStack::new();
    obj.push(-2);
    obj.push(0);
    obj.push(-3);
    println!("{}", obj.get_min());
    obj.pop();
    println!("{}", obj.top());
    println!("{}", obj.get_min());
}