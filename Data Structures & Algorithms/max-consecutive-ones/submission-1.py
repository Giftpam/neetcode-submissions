class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        occurence = []
        index = 0
        value = 0
        for i in nums:
            if i == 1:
                value += 1
                index += 1
            if i == 0:
                occurence.append(value)
                value = 0
                index +=1
            if index == len(nums):
                occurence.append(value)
                break
        return max(occurence)
