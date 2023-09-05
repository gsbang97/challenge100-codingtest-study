class Solution:
    def isValid(self, s: str) -> bool:
        stack = []


        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            else:
                if not stack:
                    return False

                top = stack.pop()
                combine = top + char
                # print(combine, stack)
                if combine not in ['()', '[]', '{}']:
                    return False


        return not stack