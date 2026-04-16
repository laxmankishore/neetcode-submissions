class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        rightProduct = [1] * len(nums)
        leftProduct = [1] * len(nums)

        for index in range(1, len(nums)):
            rightProduct[index] = nums[index - 1] * rightProduct[index - 1]
        
        for index in range(len(nums) - 2, -1, -1):
            leftProduct[index] = nums[index + 1] * leftProduct[index + 1]
        
        answer = []
        for index in range(len(nums)) :
            answer.append(rightProduct[index] * leftProduct[index])
        return answer
     

        