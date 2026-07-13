class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # pointer1 = 0
        # pointer2 = pointer1 + 1
        # while pointer1 < len(arr)-1:
        #     while pointer2 < len(arr)-1:
        #         if arr[pointer1] < arr[pointer2]:
        #             arr[pointer1], arr[pointer2] = arr[pointer2], arr[pointer1]
        #             pointer2 += 1
        #     pointer1 += 1
        #     pointer2 = pointer1 + 1
        # arr[-1] = -1
        # return arr 


        # pointer1 = len(arr) - 1
        # max_ = arr[-1]
        # for i in range(len(arr) - 2):
        #     if arr[pointer1] < max_:
        #         arr[pointer1] = max_
        #         pointer1 -= 1
        #     if arr[pointer1] > max_:
        #         max_ = arr[pointer1]
        #     arr[pointer1] = max_
        #     pointer1 -= 1
        # arr.pop(0)
        # arr.append(-1)
        # return arr


        if len(arr) == 1:
            return [-1]
        max_ = arr[-1]
        point = len(arr) - 1
        for i in arr[::-1]:
            if i >= max_:
                max_ = i
                point -= 1
            else:
                arr[point] = max_
                point -= 1
        arr.pop(0)
        arr.append(-1)
        return arr
            


