class Solution:
    def jump(self, nums: List[int]) -> int:
        # f(n) = fewest number of jumps to get to index n
        # f(n) = min(f(n-i), i = 1 - > n, nums[n-i] >= i) + 1

        # minimum array size is 1, if array is length 1 then return 0
        # we can always assume there is a valid answer
        # n^2 time, n space

        if len(nums) == 1:
            return 0

        # dp = [0] * len(nums)

        # for i in range(1, len(nums)): # guaranteed length > 1
        #     smallest = float('inf')
        #     for j in range(1, i+1):
        #         if nums[i-j] >= j:
        #             smallest = min(smallest, dp[i-j])
        #     dp[i] = smallest + 1

        # return dp[-1]

        # furthest = dict()
        # for i, dist in enumerate(nums):
        #     furthest[i] = i + dist
        
        # r = furthest[0]
        r = nums[0]
        last_r = 0
        count = 1
        while r < len(nums)-1:
            r_copy = r
            for i in range(last_r + 1, r + 1):
                r = max(r, i + nums[i])
            last_r = r_copy
            count += 1
        return count