class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = [1]
        right_product = [1]
        
        for i in range(len(nums)):
            left_product.append(left_product[-1] * nums[i])
            right_product.append(right_product[-1] * nums[len(nums) - 1 - i])

        output = []
        for i in range(len(nums)):
            output.append(left_product[i] * right_product[len(nums) - 1 - i])

        return output