class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in nums:
            if i == val:
                while val in nums:
                    nums.remove(val)
        return len(nums)



        