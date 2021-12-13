class Solution:
    def isHappy(self, n: int) -> bool:
        def rua(x: int):
            y = 0
            while x:
                y += (x % 10) ** 2
                x //= 10
            return y
        
        slow, fast = n, n
        while True:
            slow = rua(slow)
            fast = rua(fast)
            fast = rua(fast)
            if slow == fast:
                return slow == 1