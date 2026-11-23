class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            # closing bracket
            if c in closeToOpen:
                if not stack or stack.pop() != closeToOpen[c]:
                    return False
            # opening
            else:
                stack.append(c)

        return True if not stack else False