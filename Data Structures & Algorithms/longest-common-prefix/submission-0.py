class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1 or strs == []:
            return strs[0]
        else:
            strs = sorted(strs)
            first = strs[0]
            last = strs[-1]
            index = 0
            result = ""
            for i in range(len(min(strs, key = len))):
                if first[index] == last[index]:
                    result += first[index]
                    index += 1
                else:
                    break
            return result
        