class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = nums
        # n = len(nums)
        # ans.extend(nums) 
        # return ans


        # n = len(nums)
        # ans = []
        # for i in range(n):
        #     ans.append(nums[i])
        # for j in range(n):
        #     ans.append(nums[j])
        # return ans

        # ans = nums + nums
        # return ans

        #return nums + nums

        
        for j in range(len(nums)):
            nums.append(nums[j])
        return nums

        #return nums * 2


        #ans = []
