class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open  = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        for c in s:
            if c in close_to_open.values():
                stack.append(c)
            else:
                if not stack:
                    return False
                pop_c = stack.pop()
                if pop_c != close_to_open[c]:
                    return False
        return len(stack) == 0

        