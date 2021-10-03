class Solution:
    def climbStairs(self, n: int) -> int:
        def Stair(n, i, mem):
            if i > n:
                return 0
            if n - i in mem:
                return mem[n - i]
            elif n - i >= 2:
                mem[n - i] = Stair(n, i + 1, mem) + Stair(n, i + 2, mem)
            #             elif i==1:
            #                 return 1
            #             elif i==2:
            #                 return 2

            #             else:
            #                 return Stair(n,i+1)
            return mem[n - i]

        return Stair(n, 0, {1: 1, 2: 2})