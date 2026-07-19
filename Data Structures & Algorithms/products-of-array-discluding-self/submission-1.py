class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## [1,2, 4, 6] 
        ##  leftmul - [1, 1, 2, 8]
        ## rightmul = [48, 24 , 6, 1]

        rightMulArray = [1] * len(nums)
        leftMulArray = [1] * len(nums)

        index = 1
        while index < len(nums):
            leftMulArray[index] = leftMulArray[index - 1] * nums[index - 1]
            index += 1
        
        index = len(nums) - 1 - 1
        while index >= 0:
            rightMulArray[index] = rightMulArray[index + 1] * nums[index + 1]
            index -= 1
        result = []
        for index in range(len(nums)):
            result.append(leftMulArray[index] * rightMulArray[index])
        
        return result





        
        