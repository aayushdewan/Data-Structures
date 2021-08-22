class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        k = 0
        for i in range(len(nums)):
            if nums[i] != k:
                break
            k = k + 1
        return k

        # suppose the list is [3,2,0,1]
        # then after sorting it will be [0,1,2,3]
        # k initially is 0 then we can find the value after looping into the list
