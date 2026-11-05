class Solution:
    def isValid(self, s: str) -> bool:
        dict_ = {']': '[', '}': '{', ')': '('}
        stack = []
    
        for i in s:
            if i in dict_:
                if stack and stack[-1] == dict_[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False