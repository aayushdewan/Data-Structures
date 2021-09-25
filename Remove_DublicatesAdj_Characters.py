class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        if len(s) == 1:
            return s
        stack.append(s[0])
        for i in range(1, len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            elif stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])

        s = "".join(stack)
        print(s)
        return s



