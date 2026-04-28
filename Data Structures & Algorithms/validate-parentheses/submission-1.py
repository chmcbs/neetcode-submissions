class Solution:
    def isValid(self, s: str) -> bool:
        matches = {'(': ')', '[': ']', '{': '}'}
        open_brackets = []

        for i in s:
            if i in matches: # open brackets
                open_brackets.append(i)

            else: # closed brackets
                if not open_brackets or matches[open_brackets.pop()] != i: # pop removes the most recent open bracket during this check
                    return False

        return len(open_brackets) == 0