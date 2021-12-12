class Solution:
    # def decodeString(self, s: str) -> str:
    #     ans = ''
    #     cstk, estk = [], []
    #     i = 0
    #     while i < len(s):
    #         if s[i].isdigit():
    #             cnt = 0
    #             while i < len(s) and s[i].isdigit():
    #                 cnt = cnt * 10 + (ord(s[i]) - 48)
    #                 i += 1
    #             cstk.append(cnt)
    #         elif s[i] == '[':
    #             estk.append(ans)
    #             ans = ''
    #             i += 1
    #         elif s[i] == ']':
    #             # prev = [estk.pop()]
    #             # prev.extend([ans for _ in range(cstk.pop())])
    #             ans = estk.pop() + ''.join([ans for _ in range(cstk.pop())])
    #             i += 1
    #         else:
    #             ans += s[i]
    #             i += 1
    #     return ans

    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch.isdigit():
                if stack and type(stack[-1]) == int:
                    stack[-1] = stack[-1] * 10 + (ord(ch) - 48)
                else:
                    stack.append(ord(ch) - 48)
            elif ch.isalpha():
                if stack and type(stack[-1] == str) and stack[-1].isalpha():
                    stack[-1] += ch
                else:
                    stack.append(ch)
            elif ch == '[':
                stack.append(ch)
            elif ch == ']':
                tmp = []
                while stack and stack[-1] != '[':
                    tmp.append(stack.pop())
                stack.pop()
                tmp.reverse()
                stack.append(stack.pop() * ''.join(tmp))
        return ''.join(stack)


if __name__ == '__main__':
    print(Solution().decodeString('3[a]2[bc]'))
