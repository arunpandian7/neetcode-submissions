from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        b_stack = deque()
        close_to_open = {')': '(', '}': '{', ']':'['}
        for c in s:
            if c in ('(', '{', '['):
                b_stack.append(c)
            elif c in (')', '}' , ']'):
                if len(b_stack) != 0 and b_stack[-1] == close_to_open[c]:
                    b_stack.pop()
                else:
                    return False
        return len(b_stack) == 0 
            

        