class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
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