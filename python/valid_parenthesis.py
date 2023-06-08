class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        obj = {")": "(", "}": "{", "]": "["}

        for unit in s:
            if unit in obj:
                if len(stack) == 0:
                    return False
                last_item_in_stack = stack.pop()
                if last_item_in_stack != obj[unit]:
                    return False
            else:
                stack.append(unit)
        if len(stack) > 0:
            return False
        return True
