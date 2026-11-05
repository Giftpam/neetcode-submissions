class Solution:
    def isValid(self, s: str) -> bool:
        dict_ = {']': '[', '}': '{', ')': '('}
        n = len(s)
        stacks = list(s[:n//2])
        return all(dict_[s[i]] == stacks.pop() for i in range(n//2, n))